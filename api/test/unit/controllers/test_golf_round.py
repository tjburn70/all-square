import json
import copy
from unittest.mock import patch
from http import HTTPStatus

from api.models import GolfRound

GOLF_ROUND_REPO_IMPORT_PATH = "api.controllers.golf_round.golf_round_repo"
GOLF_ROUND_SERVICE_IMPORT_PATH = "api.controllers.golf_round.golf_round_service"
VERIFY_JWT_IN_REQUEST_IMPORT_PATH = "flask_jwt_extended.view_decorators.verify_jwt_in_request"
GET_JWT_IDENTITY_REQUIRED_IMPORT_PATH = "api.controllers.golf_round.get_jwt_identity"
BOTO_IMPORT_PATH = "api.controllers.golf_round.golf_round_service.boto3"


class TestGolfRoundController:

    @patch(VERIFY_JWT_IN_REQUEST_IMPORT_PATH)
    @patch(GET_JWT_IDENTITY_REQUIRED_IMPORT_PATH)
    @patch(GOLF_ROUND_REPO_IMPORT_PATH)
    def test_get_golf_rounds(
            self,
            mock_golf_round_repo,
            mock_get_jwt_identity,
            mock_verify_jwt_in_request,
            client,
            golf_round_factory,
    ):
        mock_verify_jwt_in_request.return_value = None
        user_id = 1
        mock_get_jwt_identity.return_value = user_id
        num_of_rounds = 2
        golf_rounds = [golf_round_factory(user_id=user_id) for _ in range(num_of_rounds)]
        mock_golf_round_repo.get_by_user_id.return_value = golf_rounds

        path = "/api/golf-rounds/"
        headers = {'Authorization': 'Bearer token'}
        resp = client.get(path, headers=headers)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET /golf-rounds failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert len(resp.json['result']) == num_of_rounds, f"Expecting there to be {num_of_rounds} golf rounds returned"
        assert mock_golf_round_repo.get_by_user_id.called, "Expecting golf_round_repo.get_by_user_id to be called"
        mock_golf_round_repo.get_by_user_id.assert_called_with(user_id=user_id)

    def test_get_golf_rounds_invalid_token(
            self,
            client,
    ):
        path = "/api/golf-rounds/"
        headers = {'Authorization': 'Bearer token'}
        resp = client.get(path, headers=headers)

        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
            f"GET /golf-rounds failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.UNPROCESSABLE_ENTITY}"

    @patch(VERIFY_JWT_IN_REQUEST_IMPORT_PATH)
    @patch(GET_JWT_IDENTITY_REQUIRED_IMPORT_PATH)
    @patch(GOLF_ROUND_REPO_IMPORT_PATH)
    def test_get_golf_rounds_no_data(
            self,
            mock_golf_round_repo,
            mock_get_jwt_identity,
            mock_verify_jwt_in_request,
            client,
    ):
        mock_verify_jwt_in_request.return_value = None
        user_id = 1
        mock_get_jwt_identity.return_value = user_id
        mock_golf_round_repo.get_by_user_id.return_value = []

        path = "/api/golf-rounds/"
        headers = {'Authorization': 'Bearer token'}
        resp = client.get(path, headers=headers)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET /golf-rounds failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert len(resp.json['result']) == 0, "Expecting there to be 0 golf rounds returned"
        mock_golf_round_repo.get_by_user_id.assert_called_with(user_id=user_id)

    @patch(f"{GOLF_ROUND_SERVICE_IMPORT_PATH}.GolfRoundService._queue_handicap_calculation")
    @patch(VERIFY_JWT_IN_REQUEST_IMPORT_PATH)
    @patch(GET_JWT_IDENTITY_REQUIRED_IMPORT_PATH)
    @patch(GOLF_ROUND_REPO_IMPORT_PATH)
    def test_post_golf_rounds(
            self,
            mock_golf_round_repo,
            mock_get_jwt_identity,
            mock_verify_jwt_in_request,
            mock_queue_handicap_calculation,
            client,
            test_user_id,
            content_type_header,
            golf_round_post_body_factory,
    ):
        mock_verify_jwt_in_request.return_value = None
        mock_get_jwt_identity.return_value = test_user_id

        mock_queue_handicap_calculation.return_value = None

        golf_round_post_body = golf_round_post_body_factory()
        mock_golf_round_repo.create.return_value = GolfRound(
            id=-1,
            user_id=test_user_id,
            **golf_round_post_body
        )

        path = "/api/golf-rounds/"
        auth_header = {'Authorization': 'Bearer token'}
        headers = {**auth_header, **content_type_header}
        payload = json.dumps(golf_round_post_body, default=str)
        resp = client.post(path, headers=headers, data=payload)

        assert resp.status_code == HTTPStatus.OK, \
            f"POST /golf-rounds failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert mock_golf_round_repo.create.called, "Expecting golf_round_repo.create to be called"

        expected_payload = copy.deepcopy(golf_round_post_body)
        expected_payload['user_id'] = test_user_id
        mock_golf_round_repo.create.assert_called_with(
            data=expected_payload
        )
        assert mock_queue_handicap_calculation.called
        mock_queue_handicap_calculation.assert_called_with(user_id=test_user_id)

    @patch(VERIFY_JWT_IN_REQUEST_IMPORT_PATH)
    @patch(GET_JWT_IDENTITY_REQUIRED_IMPORT_PATH)
    def test_post_golf_rounds_invalid_body(
            self,
            mock_get_jwt_identity,
            mock_verify_jwt_in_request,
            client,
            test_user_id,
            content_type_header,
    ):
        mock_verify_jwt_in_request.return_value = None
        mock_get_jwt_identity.return_value = test_user_id

        path = "/api/golf-rounds/"
        auth_header = {'Authorization': 'Bearer token'}
        headers = {**auth_header, **content_type_header}
        payload = json.dumps({"some-key": "some-value"}, default=str)
        resp = client.post(path, headers=headers, data=payload)

        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
            f"GET /golf-rounds failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.UNPROCESSABLE_ENTITY}"
