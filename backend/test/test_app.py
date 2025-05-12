from fastapi.testclient import  TestClient

from app import  app

from fastapi import  status


client = TestClient(app)


def test_return_base_path():
    res=client.get("/")
    assert  res.status_code==status.HTTP_200_OK
    assert  res.json()=={'status': 'True',"message":"We are starting with Fast API","env":"Development","function with type hint":[-1,1,3]}