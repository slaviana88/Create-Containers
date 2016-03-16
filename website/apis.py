from subprocess import check_output
from django.conf import settings
import json
import urllib.parse
import time

AUTH_KEY = settings.AUTH_KEY

CLOUD_CREATE = """request={"action":"cloudCreate",
                            "authorization_key":"%s",
                            "data":{"name":"%s",
                                    "password":"tester12345",
                                    "image_name":"Ubuntu Trusty 14.04",
                                    "datacenter_id":1,
                                    "resources":
                                                {"mem":2,"hdd":40,"cpu":2,"bw":2}}}"""

CLOUD_DETAILS = """request={"action":"cloudDetails",
                            "authorization_key":"%s",
                            "data":{"container_id":%s}}"""

ADD_SSH_KEY = """request={"action":"sshAddKey",
                          "authorization_key":"%s",
                          "data":{"key":"%s","title":"%s"}}"""

INSTALL_SSH_KEY = """request={"action":"sshInstallKey",
                              "authorization_key":"%s",
                              "data":{"key_id":%s,
                                      "container_id":%s}}"""

CLOUD_LIST = """request={"action":"cloudList",
                                 "authorization_key":"%s",
                                 "data" : {}}"""


GET_TASK = """request={"action":"getTask",
                        "authorization_key":"%s",
                        "data":{
                        "task_id":%s}}"""


def create_container(name):
    cloud_create_request = CLOUD_CREATE % (AUTH_KEY, name)
    response = json.loads(send_request(cloud_create_request))
    task_id = response["data"]["task_id"]
    return task_id


def get_details_about_container(task_id):
    get_status_request = GET_TASK % (AUTH_KEY, task_id)

    while True:
        response = json.loads(send_request(get_status_request))
        status = response["data"]["task"]["status"]
        if int(status) == 1:
            container_id = response["data"]["task"]["container_id"]
            return container_id

        time.sleep(1)


def get_container_ip(container_id):
    cloud_details_request = CLOUD_DETAILS % (AUTH_KEY, container_id)
    response = json.loads(send_request(cloud_details_request))
    container_IP = response["data"]["container"]["ip"]
    return container_IP


def add_ssh_key(ssh_key, title):
    ssh_encoded = urllib.parse.quote(ssh_key)
    add_ssh_request = ADD_SSH_KEY % (AUTH_KEY, ssh_encoded, title)
    response = json.loads(send_request(add_ssh_request))
    key_id = response["data"]["key_id"]
    return key_id


def install_ssh_key(key_id, container_id):
    install_request = INSTALL_SSH_KEY % (AUTH_KEY, key_id, container_id)
    response = json.loads(send_request(install_request))
    print(response)
    success = response["data"]["success"]
    return success == 1


def create_container_with_owner(name_container, name_owner, ssh_key):
    task_id = create_container(name_container)
    container_id = get_details_about_container(task_id)
    container_IP = get_container_ip(container_id)
    key_id = add_ssh_key(ssh_key, name_owner)
    if install_ssh_key(key_id, container_id):
        return container_IP


def send_request(request):
    command = """curl -s -k "https://api.kyup.com/client/v1" --data '{}'""".format(request)

    return check_output(["/bin/bash", "-c", command])\
        .decode('utf-8').strip()
