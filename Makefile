run:
	docker run -it -d -v --env-file .env --restart=unless-stopped --name easy_refer bot:volumes
stop:
	docker stop easy_refer
attach:
	docker attach easy_refer
dell:
	docker rm easy_refer