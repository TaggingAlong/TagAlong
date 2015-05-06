from app.api import api_blueprint

@api_blueprint.route("/tags/<path:tags>")
@api_blueprint.route("/Tags/<path:tags>")
def tags_get(tags):
	print("Getting tags {}".format(tags))
	return (tags)
