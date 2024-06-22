run:
	docker run -it -d --env-file .env --restart=unless-stopped --name easy_refer easy_bot_image
stop:
	docker stop easy_refer
attach:
	docker attach easy_refer
dell:
	docker rm easy_refer