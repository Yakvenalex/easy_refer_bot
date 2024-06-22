run:
	docker run -it -d --env-file .env --name easy_refer easy_refer_bot
stop:
	docker stop easy_refer
attach:
	docker attach easy_refer
dell:
	docker rm easy_refer