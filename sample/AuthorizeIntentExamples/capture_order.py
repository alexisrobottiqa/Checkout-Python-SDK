from checkoutsdk.payments import AuthorizationsCaptureRequest
from sample import SampleSkeleton


class CaptureOrder(SampleSkeleton):
    """Sample to Capture Order"""
    @staticmethod
    def build_request_body():
        """Method to build empty body"""
        return {}

    def capture_order(self, authorization_id, debug=False):
        """Method to capture order using authorization_id"""
        request = AuthorizationsCaptureRequest(authorization_id)
        request.request_body(self.build_request_body())
        response = self.client.execute(request)
        if debug:
            print 'Status Code: ', response.status_code
            print 'Status: ', response.result.status
            print 'Capture ID: ', response.result.id
            print 'Links: '
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
        return response


if __name__ == "__main__":
    auth_id = '8S628606RY839401M'
    CaptureOrder().capture_order(auth_id, debug=True)
