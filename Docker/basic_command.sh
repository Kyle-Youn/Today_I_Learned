#!/bin/bash

# 도커 이미지를 기반으로 새 컨테이너를 실행합니다.
docker run -it --name my-container ubuntu /bin/bash     # Ubuntu 기본 이미지를 사용, 컨테이너 실행 시 /bin/bash 명령 실행


# 현재 실행 중인 컨테이너 목록을 확인
docker ps
# 모든 컨테이너(종료된 컨테이너 포함)를 확인
docker ps -a


# 로컬에 저장되어 있는 도커 이미지 목록을 확인
docker images
