# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Cdr(models.Model):
    id = models.BigIntegerField(primary_key=True)
    calldate = models.DateTimeField()
    clid = models.CharField(max_length=80)
    src = models.CharField(max_length=80)
    dst = models.CharField(max_length=80)
    dcontext = models.CharField(max_length=80)
    channel = models.CharField(max_length=80)
    dstchannel = models.CharField(max_length=80)
    lastapp = models.CharField(max_length=80)
    lastdata = models.CharField(max_length=80)
    duration = models.IntegerField()
    billsec = models.IntegerField()
    disposition = models.CharField(max_length=45)
    amaflags = models.IntegerField()
    accountcode = models.CharField(max_length=20)
    uniqueid = models.CharField(max_length=32)
    userfield = models.CharField(max_length=255)
    servidor = models.CharField(max_length=255, blank=True)
    gravacao = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=3, blank=True)
    perfil = models.CharField(max_length=20, blank=True)
    did = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'cdr'


class Musiconhold(models.Model):
    name = models.CharField(primary_key=True, max_length=80)
    mode = models.CharField(max_length=80, blank=True)
    directory = models.CharField(max_length=255, blank=True)
    application = models.CharField(max_length=255, blank=True)
    digit = models.CharField(max_length=1, blank=True)
    sort = models.CharField(max_length=10, blank=True)
    format = models.CharField(max_length=10, blank=True)
    stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'musiconhold'


class QueueLog(models.Model):
    time = models.DateTimeField(blank=True, null=True)
    callid = models.CharField(max_length=50, blank=True)
    queuename = models.CharField(max_length=50, blank=True)
    agent = models.CharField(max_length=50, blank=True)
    event = models.CharField(max_length=20, blank=True)
    data1 = models.CharField(max_length=50, blank=True)
    data2 = models.CharField(max_length=50, blank=True)
    data3 = models.CharField(max_length=50, blank=True)
    data4 = models.CharField(max_length=50, blank=True)
    data5 = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'queue_log'


class QueueMemberTable(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    membername = models.CharField(max_length=40, blank=True)
    queue_name = models.CharField(max_length=128, blank=True)
    interface = models.CharField(max_length=128, blank=True)
    penalty = models.IntegerField(blank=True, null=True)
    paused = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queue_member_table'


class QueueTable(models.Model):
    name = models.CharField(primary_key=True, max_length=128)
    musiconhold = models.CharField(max_length=128, blank=True)
    announce = models.CharField(max_length=128, blank=True)
    context = models.CharField(max_length=128, blank=True)
    timeout = models.IntegerField(blank=True, null=True)
    monitor_join = models.IntegerField(blank=True, null=True)
    monitor_format = models.CharField(max_length=128, blank=True)
    queue_youarenext = models.CharField(max_length=128, blank=True)
    queue_thereare = models.CharField(max_length=128, blank=True)
    queue_callswaiting = models.CharField(max_length=128, blank=True)
    queue_holdtime = models.CharField(max_length=128, blank=True)
    queue_minutes = models.CharField(max_length=128, blank=True)
    queue_seconds = models.CharField(max_length=128, blank=True)
    queue_lessthan = models.CharField(max_length=128, blank=True)
    queue_thankyou = models.CharField(max_length=128, blank=True)
    queue_reporthold = models.CharField(max_length=128, blank=True)
    announce_frequency = models.IntegerField(blank=True, null=True)
    announce_round_seconds = models.IntegerField(blank=True, null=True)
    announce_holdtime = models.CharField(max_length=128, blank=True)
    retry = models.IntegerField(blank=True, null=True)
    wrapuptime = models.IntegerField(blank=True, null=True)
    maxlen = models.IntegerField(blank=True, null=True)
    servicelevel = models.IntegerField(blank=True, null=True)
    strategy = models.CharField(max_length=128, blank=True)
    joinempty = models.CharField(max_length=128, blank=True)
    leavewhenempty = models.CharField(max_length=128, blank=True)
    eventmemberstatus = models.IntegerField(blank=True, null=True)
    eventwhencalled = models.IntegerField(blank=True, null=True)
    reportholdtime = models.IntegerField(blank=True, null=True)
    memberdelay = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    timeoutrestart = models.IntegerField(blank=True, null=True)
    periodic_announce = models.CharField(max_length=50, blank=True)
    periodic_announce_frequency = models.IntegerField(blank=True, null=True)
    ringinuse = models.IntegerField(blank=True, null=True)
    setinterfacevar = models.IntegerField(blank=True, null=True)
    cliente_id = models.IntegerField()
    descricao = models.CharField(max_length=30)
    redirto = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'queue_table'


class SipDevices(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=10)
    ipaddr = models.CharField(max_length=15, blank=True)
    port = models.IntegerField(blank=True, null=True)
    regseconds = models.IntegerField(blank=True, null=True)
    defaultuser = models.CharField(max_length=50, blank=True)
    fullcontact = models.CharField(max_length=35, blank=True)
    regserver = models.CharField(max_length=20, blank=True)
    useragent = models.CharField(max_length=20, blank=True)
    lastms = models.IntegerField(blank=True, null=True)
    host = models.CharField(max_length=40, blank=True)
    type = models.CharField(max_length=6, blank=True)
    context = models.CharField(max_length=40, blank=True)
    permit = models.CharField(max_length=40, blank=True)
    deny = models.CharField(max_length=40, blank=True)
    secret = models.CharField(max_length=40, blank=True)
    md5secret = models.CharField(max_length=40, blank=True)
    remotesecret = models.CharField(max_length=40, blank=True)
    transport = models.CharField(max_length=7, blank=True)
    dtmfmode = models.CharField(max_length=9, blank=True)
    directmedia = models.CharField(max_length=6, blank=True)
    nat = models.CharField(max_length=18, blank=True)
    callgroup = models.CharField(max_length=40, blank=True)
    pickupgroup = models.CharField(max_length=40, blank=True)
    language = models.CharField(max_length=40, blank=True)
    disallow = models.CharField(max_length=40, blank=True)
    allow = models.CharField(max_length=40, blank=True)
    insecure = models.CharField(max_length=40, blank=True)
    trustrpid = models.CharField(max_length=3, blank=True)
    progressinband = models.CharField(max_length=5, blank=True)
    promiscredir = models.CharField(max_length=3, blank=True)
    useclientcode = models.CharField(max_length=3, blank=True)
    accountcode = models.CharField(max_length=40, blank=True)
    setvar = models.CharField(max_length=255, blank=True)
    callerid = models.CharField(max_length=40, blank=True)
    amaflags = models.CharField(max_length=40, blank=True)
    callcounter = models.CharField(max_length=3, blank=True)
    busylevel = models.IntegerField(blank=True, null=True)
    allowoverlap = models.CharField(max_length=3, blank=True)
    allowsubscribe = models.CharField(max_length=3, blank=True)
    videosupport = models.CharField(max_length=3, blank=True)
    maxcallbitrate = models.IntegerField(blank=True, null=True)
    rfc2833compensate = models.CharField(max_length=3, blank=True)
    mailbox = models.CharField(max_length=40, blank=True)
    session_timers = models.CharField(db_column='session-timers', max_length=9, blank=True)  # Field renamed to remove unsuitable characters.
    session_expires = models.IntegerField(db_column='session-expires', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    session_minse = models.IntegerField(db_column='session-minse', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    session_refresher = models.CharField(db_column='session-refresher', max_length=3, blank=True)  # Field renamed to remove unsuitable characters.
    t38pt_usertpsource = models.CharField(max_length=40, blank=True)
    regexten = models.CharField(max_length=40, blank=True)
    fromdomain = models.CharField(max_length=40, blank=True)
    fromuser = models.CharField(max_length=40, blank=True)
    realm = models.CharField(max_length=60, blank=True)
    qualify = models.CharField(max_length=40, blank=True)
    defaultip = models.CharField(max_length=40, blank=True)
    rtptimeout = models.IntegerField(blank=True, null=True)
    rtpholdtimeout = models.IntegerField(blank=True, null=True)
    sendrpid = models.CharField(max_length=3, blank=True)
    outboundproxy = models.CharField(max_length=40, blank=True)
    callbackextension = models.CharField(max_length=40, blank=True)
    registertrying = models.CharField(max_length=3, blank=True)
    timert1 = models.IntegerField(blank=True, null=True)
    timerb = models.IntegerField(blank=True, null=True)
    qualifyfreq = models.IntegerField(blank=True, null=True)
    constantssrc = models.CharField(max_length=3, blank=True)
    contactpermit = models.CharField(max_length=40, blank=True)
    contactdeny = models.CharField(max_length=40, blank=True)
    usereqphone = models.CharField(max_length=3, blank=True)
    textsupport = models.CharField(max_length=3, blank=True)
    faxdetect = models.CharField(max_length=3, blank=True)
    buggymwi = models.CharField(max_length=3, blank=True)
    auth = models.CharField(max_length=40, blank=True)
    fullname = models.CharField(max_length=40, blank=True)
    trunkname = models.CharField(max_length=40, blank=True)
    cid_number = models.CharField(max_length=40, blank=True)
    callingpres = models.CharField(max_length=21, blank=True)
    mohinterpret = models.CharField(max_length=40, blank=True)
    mohsuggest = models.CharField(max_length=40, blank=True)
    parkinglot = models.CharField(max_length=40, blank=True)
    hasvoicemail = models.CharField(max_length=3, blank=True)
    subscribemwi = models.CharField(max_length=3, blank=True)
    vmexten = models.CharField(max_length=40, blank=True)
    autoframing = models.CharField(max_length=3, blank=True)
    rtpkeepalive = models.IntegerField(blank=True, null=True)
    call_limit = models.IntegerField(db_column='call-limit', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    g726nonstandard = models.CharField(max_length=3, blank=True)
    ignoresdpversion = models.CharField(max_length=3, blank=True)
    allowtransfer = models.CharField(max_length=3, blank=True)
    dynamic = models.CharField(max_length=3, blank=True)
    alias = models.CharField(max_length=5, blank=True)
    alias_name = models.CharField(max_length=20, blank=True)
    gravacao = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'sip_devices'


class Voicemail(models.Model):
    uniqueid = models.IntegerField(primary_key=True)
    context = models.CharField(max_length=80)
    mailbox = models.CharField(max_length=80)
    password = models.CharField(max_length=80)
    fullname = models.CharField(max_length=80, blank=True)
    email = models.CharField(max_length=80, blank=True)
    pager = models.CharField(max_length=80, blank=True)
    attach = models.CharField(max_length=3, blank=True)
    attachfmt = models.CharField(max_length=10, blank=True)
    serveremail = models.CharField(max_length=80, blank=True)
    language = models.CharField(max_length=20, blank=True)
    tz = models.CharField(max_length=30, blank=True)
    deletevoicemail = models.CharField(max_length=3, blank=True)
    saycid = models.CharField(max_length=3, blank=True)
    sendvoicemail = models.CharField(max_length=3, blank=True)
    review = models.CharField(max_length=3, blank=True)
    tempgreetwarn = models.CharField(max_length=3, blank=True)
    operator = models.CharField(max_length=3, blank=True)
    envelope = models.CharField(max_length=3, blank=True)
    sayduration = models.CharField(max_length=3, blank=True)
    saydurationm = models.IntegerField(blank=True, null=True)
    forcename = models.CharField(max_length=3, blank=True)
    forcegreetings = models.CharField(max_length=3, blank=True)
    callback = models.CharField(max_length=80, blank=True)
    dialout = models.CharField(max_length=80, blank=True)
    exitcontext = models.CharField(max_length=80, blank=True)
    maxmsg = models.IntegerField(blank=True, null=True)
    volgain = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    imapuser = models.CharField(max_length=80, blank=True)
    imappassword = models.CharField(max_length=80, blank=True)
    stamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'voicemail'
