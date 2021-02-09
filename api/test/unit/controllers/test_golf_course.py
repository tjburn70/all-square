import json
import copy
from unittest.mock import patch
from http import HTTPStatus

import pytest

GOLF_COURSE_REPO_IMPORT_PATH = "api.controllers.golf_course.golf_course_repo"
TEE_BOX_REPO_IMPORT_PATH = "api.controllers.golf_course.tee_box_repo"
HOLE_REPO_IMPORT_PATH = "api.controllers.golf_course.hole_repo"


class TestGolfCourseController:

    @patch(GOLF_COURSE_REPO_IMPORT_PATH)
    def test_get_all_golf_courses(
            self,
            mock_golf_course_repo,
            client,
            golf_course_model,
    ):
        mock_golf_course_repo.get_all.return_value = [golf_course_model]

        path = "/api/golf-courses/"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET /golf-courses failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert len(resp.json['result']) == 1, "Expecting there to be 2 golf courses returned"
        assert mock_golf_course_repo.get_all.called, "Expecting golf_course_repo.get_all to be called"

    @patch(GOLF_COURSE_REPO_IMPORT_PATH)
    def test_get_golf_courses_by_ids(
            self,
            mock_golf_course_repo,
            client,
            olympia_fields_north_course_id,
            olympia_fields_south_course_id,
            olympia_fields_north_course,
            olympia_fields_south_course,
    ):
        mock_golf_course_repo.get_by_ids.return_value = [
            olympia_fields_north_course,
            olympia_fields_south_course,
        ]
        path = f"/api/golf-courses/?id={olympia_fields_north_course_id}&id={olympia_fields_south_course_id}"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert mock_golf_course_repo.get_by_ids.called, "Expecting golf_course_repo.get_by_ids to be called"
        expected_ids = [str(olympia_fields_north_course_id), str(olympia_fields_south_course_id)]
        mock_golf_course_repo.get_by_ids.assert_called_with(ids=expected_ids)

    @patch(GOLF_COURSE_REPO_IMPORT_PATH)
    def test_get_golf_courses_by_id(
            self,
            mock_golf_course_repo,
            client,
            olympia_fields_north_course_id,
            olympia_fields_north_course,
    ):
        mock_golf_course_repo.get.return_value = [olympia_fields_north_course]
        path = f"/api/golf-courses/{olympia_fields_north_course_id}"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert mock_golf_course_repo.get.called, "Expecting golf_course_repo.get_by_ids to be called"
        mock_golf_course_repo.get.assert_called_with(olympia_fields_north_course_id)

    @patch(GOLF_COURSE_REPO_IMPORT_PATH)
    def test_delete_golf_courses_by_id(
            self,
            mock_golf_course_repo,
            client,
            golf_course_id,
    ):
        mock_golf_course_repo.delete.return_value = True
        path = f"/api/golf-courses/{golf_course_id}"
        resp = client.delete(path)

        assert resp.status_code == HTTPStatus.NO_CONTENT, \
            f"DELETE {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.NO_CONTENT}"
        assert mock_golf_course_repo.delete.called, "Expecting golf_course_repo.get_by_ids to be called"
        mock_golf_course_repo.delete.assert_called_with(model_id=golf_course_id)

    @patch(TEE_BOX_REPO_IMPORT_PATH)
    def test_get_tee_boxes_by_golf_course_id(
            self,
            mock_tee_box_repo,
            client,
            golf_course_id,
            blue_tee_box,
    ):
        mock_tee_box_repo.get_by_golf_course_id.return_value = [blue_tee_box]
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert len(resp.json['result']) == 1, "Expecting there to be 1 tee-box returned"
        assert mock_tee_box_repo.get_by_golf_course_id.called, \
            "Expecting tee_box_repo.get_by_golf_course_id to be called"
        mock_tee_box_repo.get_by_golf_course_id.assert_called_with(golf_course_id=golf_course_id)

    def test_add_tee_box_no_content_header(
            self,
            client,
            golf_course_id,
    ):
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes"
        resp = client.post(path, headers=None, data={})
        assert resp.status_code == HTTPStatus.BAD_REQUEST, \
            f"If no Content-Type header in POST call, expect to receive a status_code: {HTTPStatus.BAD_REQUEST}"

    def test_add_tee_box_invalid_body(
            self,
            client,
            golf_course_id,
    ):
        payload = {"random_key": "I need more fields!"}
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes"
        resp = client.post(path, json=payload)
        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
            f"If payload is missing required fields, " \
            f"expected to receive a status_code: {HTTPStatus.UNPROCESSABLE_ENTITY}"

    @pytest.mark.skip("temporarily skip for now")
    @patch(TEE_BOX_REPO_IMPORT_PATH)
    def test_add_tee_boxes_by_golf_course_id(
            self,
            mock_tee_box_repo,
            client,
            golf_course_id,
            tee_box_dict,
            tee_box_model,
            content_type_header,
    ):
        mock_tee_box_repo.get_by_golf_course_id.return_value = [tee_box_model]
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes"
        payload = json.dumps(tee_box_dict, default=str)
        resp = client.post(path, headers=content_type_header, data=payload)

        assert resp.status_code == HTTPStatus.OK, \
            f"POST {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert mock_tee_box_repo.create.called, \
            "Expecting tee_box_repo.add to be called"

        expected_payload = copy.deepcopy(tee_box_dict)
        expected_payload['golf_course_id'] = golf_course_id

        mock_tee_box_repo.create.assert_called_with(data=golf_course_id)

    @patch(TEE_BOX_REPO_IMPORT_PATH)
    def test_get_tee_boxes_by_id(
            self,
            mock_tee_box_repo,
            client,
            tee_box_id,
            tee_box_model,
    ):
        mock_tee_box_repo.get.return_value = [tee_box_model]
        path = f"/api/golf-courses/tee-boxes/{tee_box_id}"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"

        assert mock_tee_box_repo.get.called, \
            "Expecting tee_box_repo.get to be called"
        mock_tee_box_repo.get.assert_called_with(tee_box_id)

    @patch(TEE_BOX_REPO_IMPORT_PATH)
    def test_delete_tee_boxes(
            self,
            mock_tee_box_repo,
            client,
            tee_box_id,
            tee_box_model,
    ):
        mock_tee_box_repo.delete.return_value = True
        path = f"/api/golf-courses/tee-boxes/{tee_box_id}"
        resp = client.delete(path)

        assert resp.status_code == HTTPStatus.NO_CONTENT, \
            f"DELETE {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.NO_CONTENT}"

        assert mock_tee_box_repo.delete.called, \
            "Expecting tee_box_repo.delete to be called"
        mock_tee_box_repo.delete.assert_called_with(model_id=tee_box_id)

    @patch(TEE_BOX_REPO_IMPORT_PATH)
    def test_delete_tee_boxes_failed(
            self,
            mock_tee_box_repo,
            client,
            tee_box_id,
            tee_box_model,
    ):
        mock_tee_box_repo.delete.return_value = False
        path = f"/api/golf-courses/tee-boxes/{tee_box_id}"
        resp = client.delete(path)

        assert resp.status_code == HTTPStatus.BAD_REQUEST, \
            f"DELETE {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.BAD_REQUEST}"

        assert mock_tee_box_repo.delete.called, \
            "Expecting tee_box_repo.delete to be called"
        mock_tee_box_repo.delete.assert_called_with(model_id=tee_box_id)

    @patch(HOLE_REPO_IMPORT_PATH)
    def test_get_holes_by_tee_box_id(
            self,
            mock_hole_repo,
            client,
            golf_course_id,
            tee_box_id,
            holes_18,
    ):
        mock_hole_repo.get_by_tee_box_id.return_value = holes_18
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes/{tee_box_id}/holes"
        resp = client.get(path)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"
        assert len(resp.json['result']) == 18, "Expecting there to be 18 holes returned"
        assert mock_hole_repo.get_by_tee_box_id.called, \
            "Expecting hole_repo.get_by_tee_box_id to be called"
        mock_hole_repo.get_by_tee_box_id.assert_called_with(tee_box_id=tee_box_id)

    @patch(HOLE_REPO_IMPORT_PATH)
    def test_add_holes(
            self,
            mock_hole_repo,
            client,
            golf_course_id,
            tee_box_id,
            holes_post_body,
    ):
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes/{tee_box_id}/holes"
        resp = client.post(path, json=holes_post_body)

        assert resp.status_code == HTTPStatus.OK, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.OK}"

        assert mock_hole_repo.bulk_create.called, \
            "Expecting mock_hole_repo.bulk_create to be called"

        expected_data = [
            {
                'golf_course_id': golf_course_id,
                'tee_box_id': tee_box_id,
                **hole
            }
            for hole in holes_post_body['holes']
        ]
        mock_hole_repo.bulk_create.assert_called_with(records=expected_data)

    def test_add_holes_invalid_schema(
            self,
            client,
            golf_course_id,
            tee_box_id,
    ):
        payload = {
            'holes': [
                {'some-key': 'some-value'}
            ]
        }
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes/{tee_box_id}/holes"
        resp = client.post(path, json=payload)

        assert resp.status_code == HTTPStatus.UNPROCESSABLE_ENTITY, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.UNPROCESSABLE_ENTITY}"

    def test_add_holes_no_holes_key(
            self,
            client,
            golf_course_id,
            tee_box_id,
    ):
        path = f"/api/golf-courses/{golf_course_id}/tee-boxes/{tee_box_id}/holes"
        bad_payload = {'some_key': 'some-value'}
        resp = client.post(path, json=bad_payload)

        assert resp.status_code == HTTPStatus.BAD_REQUEST, \
            f"GET {path} failed with status_code = {resp.status_code}, " \
            f"expected to receive a status_code: {HTTPStatus.BAD_REQUEST}"
