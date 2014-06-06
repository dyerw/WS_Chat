from autobahn.twisted.wamp import ApplicationSession

class AppSession(ApplicationSession):

   def onJoin(self, details):
        def log_msg(msg):
            with open(os.path.join('web', 'log.html'), 'a') as log_file:
                log_file.write(msg)

        yield self.subsribe(log_msg, 'com.examples.groupchat')
