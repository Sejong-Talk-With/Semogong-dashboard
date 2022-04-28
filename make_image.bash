docker build --platform amd64 --build-arg DEPENDENCY=build/dependency -t wjdqlsdlsp/make_dashboard:$1 .

#버전관리용 도커허브로 전송
images_id=$(docker images -qa wjdqlsdlsp/make_dashboard:$1)
docker tag $images_id wjdqlsdlsp/make_dashboard:$1
docker push wjdqlsdlsp/make_dashboard:$1