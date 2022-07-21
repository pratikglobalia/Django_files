from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init, pre_save, pre_delete, post_init, post_save, post_delete, pre_migrate, post_migrate
from django.core.signals import request_started, request_finished, got_request_exception
from django.db.backends.signals import connection_created


@receiver(user_logged_in, sender=User)
def login_success(sender, request, user, **kwargs):
    print('---------------------------------')
    print('logged-in signal....run intro....')
    print('sender :',sender)
    print('request :',request)
    print('user :',user)
    print(f'kwargs : {kwargs}')
# user_logged_in.connect(login_success, sender=User)


@receiver(user_logged_out, sender=User)
def log_out(sender, request, user, **kwargs):
    print('---------------------------------')
    print('log-out signal....run outro....')
    print('sender :',sender)
    print('request :',request)
    print('user :',user)
    print(f'kwargs : {kwargs}')
# user_logged_out.connect(log_out, sender=User)


@receiver(user_login_failed)
def login_failed(sender, credentials, request, **kwargs):
    print('---------------------------------')
    print('login-failed signal..')
    print('sender :',sender)
    print('credentials :',credentials)
    print('request :',request)
    print(f'kwargs : {kwargs}')
# user_login_failed.connect(login_failed)


@receiver(pre_save, sender=User)
def at_begining_save(sender, instance, **kwargs):
    print('---------------------------------')
    print('pre-save signal..')
    print('sender :',sender)
    print('instance :',instance)
    print(f'kwargs : {kwargs}')
# pre_save.connect(at_begining_save, sender=User)


@receiver(post_save, sender=User)
def at_ending_save(sender, instance, created, **kwargs):
    if created:
        print('---------------------------------')
        print('post-save signal..')
        print('newrecord...')
        print('sender :',sender)
        print('instance :',instance)
        print('created :',created)
        print(f'kwargs : {kwargs}')
    else:
        print('---------------------------------')
        print('post-save signal..')
        print('upadte..')
        print('sender :',sender)
        print('instance :',instance)
        print('created :',created)
        print(f'kwargs : {kwargs}')
        
        
@receiver(pre_delete, sender=User)
def at_begining_delete(sender, instance, **kwargs):
    print('---------------------------------')
    print('pre-delete signal..')
    print('sender :',sender)
    print('instance :',instance)
    print(f'kwargs : {kwargs}')
    
    
@receiver(post_delete, sender=User)
def at_ending_delete(sender, instance, **kwargs):
    print('---------------------------------')
    print('post-delete signal..')
    print('sender :',sender)
    print('instance :',instance)
    print(f'kwargs : {kwargs}')
    
    
@receiver(pre_init, sender=User)
def at_begining_init(sender, *arg, **kwargs):
    print('---------------------------------')
    print('pre-init signal..')
    print('sender :',sender)
    print(f'arg :{arg}')
    print(f'kwargs : {kwargs}')
    
    
@receiver(post_init, sender=User)
def at_ending_init(sender, *arg, **kwargs):
    print('---------------------------------')
    print('post-init signal..')
    print('sender :',sender)
    print(f'arg :{arg}')
    print(f'kwargs : {kwargs}')
    
    
@receiver(request_started)
def at_start(sender, environ, **kwargs):
    print('---------------------------------')
    print('request-started signal..')
    print('sender :',sender)
    print('environ :',environ)
    print(f'kwargs : {kwargs}')
    
    
@receiver(request_finished)
def at_finish(sender, **kwargs):
    print('---------------------------------')
    print('request-finished signal..')
    print('sender :',sender)
    print(f'kwargs : {kwargs}')
    
    
@receiver(got_request_exception)
def at_req_exception(sender, request, **kwargs):
    print('---------------------------------')
    print('request-exception signal..')
    print('sender :',sender)
    print('request :',request)
    print(f'kwargs : {kwargs}')
    
    
@receiver(pre_migrate)
def before_install_app(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------------------')
    print('before_install_app signal..')
    print('sender :',sender)
    print('app_config :',app_config)
    print('verbosity :',verbosity)
    print('interactive :',interactive)
    print('using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'kwargs : {kwargs}')
    
    
@receiver(post_migrate)
def end_migrate(sender, app_config, verbosity, interactive, using, plan, apps, **kwargs):
    print('---------------------------------')
    print('end_migrate signal..')
    print('sender :',sender)
    print('app_config :',app_config)
    print('verbosity :',verbosity)
    print('interactive :',interactive)
    print('using :',using)
    print('plan :',plan)
    print('apps :',apps)
    print(f'kwargs : {kwargs}')
    
    
@receiver(connection_created)
def conn_db(sender, connection, **kwargs):
    print('---------------------------------')
    print('database-connection signal..')
    print('sender :',sender)
    print('connection :',connection)
    print(f'kwargs : {kwargs}')