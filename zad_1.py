import requests
import random

ENDPOINT = "https://todo.pixegami.io"

def test_can_call_api():
    response = requests.get(url=ENDPOINT)
    code_response = response.status_code
    assert code_response == 200

def test_api_returns_404_for_bad_url():
    """GET https://todo.pixegami.io/status
       should return 404 """
    response = requests.get(url=ENDPOINT + "/status")
    assert response.status_code == 404

def test_api_returns_hello_msg():
    """Body should return hello world... msg
       '{"message":"Hello World from Todo API"}'"""
    expected = "Hello World from Todo API"
    response = requests.get(url=ENDPOINT)
    body = response.json()
    # print(body)
    # print(expected)
    assert expected == body["message"]

def test_api_returns_not_found_for_bad_url():
    response = requests.get(url=ENDPOINT + "/status")
    body = response.json()
    expected = "Not Found"
    # print(body)
    # print(expected)
    assert expected == body["detail"]

def test_api_returns_not_found_for_bad_url2():
    """
    1. get response for GET https://todo.pixegami.io/status
    2. get body from response
    3. body should contain "Not Found"
    body: {"detail":"Not Found"}
    """
    bad_url = ENDPOINT + "/nieistnieje"
    response = requests.get(bad_url)
    body = response.json()
    expected = {"detail":"Not Found"}
    assert expected == body

def test_can_create_task():
    """PUT https://todo.pixegami.io/create-task + body
    response body:
    {'task':
        {'user_id': 'Alamakota',
        'content': 'Nakarm kota',
        'is_done': False,
        'created_time': 1752307995,
        'task_id': 'task_fb0c7dc55175469bab1e2699dbbd6653',
        'ttl': 1752394395
        }
    }
    """
    req_body = {"content": "Nakarm kota",
                "user_id": "Alamakota",
                "task_id": "01",
                "is_done": False
               }
    response_put = requests.put(url=ENDPOINT + "/create-task", json=req_body)
    assert response_put.status_code == 200

    response_body = response_put.json()
    assert response_body["task"]["user_id"] == "Alamakota"
    assert response_body["task"]["content"] == "Nakarm kota"
    assert response_body["task"]["is_done"] == False


"""{'is_done': False,
    'content': 'Nakarm kota',
    'ttl': 1752394395,
    'user_id': 'Alamakota',
    'task_id': 'task_fb0c7dc55175469bab1e2699dbbd6653',
    'created_time': 1752307995
    }
    """

def test_not_existing_task_id_returns_404():
    response = requests.get(url=ENDPOINT + "/get-task/" + "task_not_existing")
    assert response.status_code == 404


def test_can_create_and_get_task():
    """GET https://todo.pixegami.io/get-task/{task_id}
    1. create task
    2. extract unique_task_id
    3. Use unique_task_id from 2. to test get-task
    """
    #1
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_tmp",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    #2
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]
    # print("\n")
    # print(unique_task_id)

    #3
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    assert response.json()['task_id'] == unique_task_id

def test_can_list_tasks():
    """GET https://todo.pixegami.io/list-tasks/Alamakota_tmp2
    Napisz test do wylistowania tasks
    """
    radom_user = "Alamakota_tmp_" + str(random.randint(1000000, 9999999))
    task_body = {"content": "Nakarm kota",
                 "user_id": radom_user,
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200

    response = requests.get(url=ENDPOINT + "/list-tasks/" + radom_user)
    assert response.status_code == 200

    body = response.json()
    tasks = body["tasks"]
    assert isinstance(tasks, list)
    assert len(tasks) > 0

def test_can_update_task():
    """
    1. create task
    2. update task
    3. check if updated
    """
    #1
    task_body = {"content": "Nakarm kota",
                 "user_id": "Alamakota_1",
                 "task_id": "01",
                 "is_done": False
                }
    response_create = requests.put(url=ENDPOINT + "/create-task", json=task_body)
    assert response_create.status_code == 200
    body_create_response = response_create.json()
    unique_task_id = body_create_response["task"]["task_id"]

    #2
    updated_body = {"content": "Nakarm kota",
                    "user_id": "Alamakota_1",
                    "task_id": unique_task_id,
                    "is_done": True
                    }
    response_update = requests.put(url=ENDPOINT + "/update-task", json=updated_body)
    assert response_update.status_code == 200

    #3
    response = requests.get(url=ENDPOINT + "/get-task/" + unique_task_id)
    assert response.status_code == 200
    body = response.json()
    assert body["is_done"] == True

def test_can_delete_task():
    """
    1. create task
    2. extract task_id
    3. delete task
    4. get task and expect deleted
    """