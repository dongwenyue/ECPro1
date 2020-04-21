from faker import Faker

from utils.stringIO.logger.testlogger import DEBUG
from utils.testutils.faker.gen_idcard import gen_idcard

global FAKER
FAKER = Faker(locale='ZH_CN')


def idnum():
    idnum = gen_idcard()
    DEBUG('generate random id number by faker :%s' % idnum)
    return idnum


def phone():
    mobile = FAKER.phone_number()  # @UndefinedVariable
    DEBUG('generate random phone number by faker :%s' % mobile)
    return mobile


def fullname():
    name = FAKER.name()  # @UndefinedVariable
    DEBUG('generate random name by faker :%s' % name)
    return name
