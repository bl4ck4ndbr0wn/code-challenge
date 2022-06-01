import json

from rest_framework.renderers import JSONRenderer


class MultipleJSONRenderer(JSONRenderer):
    charset = 'utf-8'

    def render(self, data, media_type=None, renderer_context=None):
        # We want the default JSONRenderer to handle rendering
        # integer and strings and If the view throws an error,
        #`data` will contain an `errors` key, so we need to
        # check for this case.

        if isinstance(data, dict):
            errors = data.get('errors', None)

            if errors is not None:
                # As mentioned about, we will let the default JSONRenderer handle
                # rendering errors.
                return json.dumps(data)

        if isinstance(data, int):
            return json.dumps({
                "data": data,
                'message': "Is neither a multiple of 5 not 7." ,
            })

        return json.dumps({
            "data": data,
        })
