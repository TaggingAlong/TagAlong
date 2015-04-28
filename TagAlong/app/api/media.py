from app.api import api_blueprint

@api_blueprint.route("/media/<path:id>")
@api_blueprint.route("/Media/<path:id>")
def media_get(id):
    print("Getting media {}".format(id))
    return (id)