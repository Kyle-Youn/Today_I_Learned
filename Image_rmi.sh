#!/bin/bash

# 현재 이미지 확인
docker images


# 이미지 삭제
docker rmi [이미지id]


# 특정 버전 삭제
docker rmi postgres:12.1
