import random

class PrimaryReplicaRouter:

    def db_for_read(self, model, **hints):
    # read from another db (different from insertion db)
    # return random.choice(['replica1', 'replica2'])
        return 'primary'

    def db_for_write(self, model, **hints):
        return 'primary'

    def allow_relation(self, obj1, obj2, **hints):
    #
    #    db_list = ('primary', 'replica1', 'replica2')
    #    if obj1._state_db in db_list or obj2._state_db in db_list:
    #        return True
        db = 'primary'
        if obj1._state_db == db or obj2._state_db == db:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return True
