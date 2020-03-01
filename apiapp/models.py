# coding: utf-8
from sqlalchemy import Column, Float, ForeignKey, Integer, MetaData, String, Text, VARBINARY
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql.types import BIT, LONGBLOB
from sqlalchemy.schema import FetchedValue
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata



class ACharge(Base):
    __tablename__ = 'a_charge'

    id = Column(Integer, primary_key=True)
    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    gold = Column(Integer)

    a = relationship('CArticle', primaryjoin='ACharge.a_id == CArticle.a_id', backref='a_charges')



class CATag(Base):
    __tablename__ = 'c_a_tag'

    a_id = Column(Integer, primary_key=True)
    t_name = Column(String(30))



class CArticle(Base):
    __tablename__ = 'c_article'

    a_id = Column(Integer, primary_key=True)
    i_id = Column(ForeignKey('c_images.i_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    name = Column(String(70))
    number = Column(Integer)
    status = Column(String(5))
    isfree = Column(BIT(1))
    fabulous = Column(Integer)
    profit = Column(Float)
    details = Column(Text)
    date = Column(String(50))

    i = relationship('CImage', primaryjoin='CArticle.i_id == CImage.i_id', backref='c_articles')
    m = relationship('CMusic', primaryjoin='CArticle.m_id == CMusic.m_id', backref='c_articles')
    u = relationship('User', primaryjoin='CArticle.u_id == User.u_id', backref='c_articles')



class CArticleTag(Base):
    __tablename__ = 'c_article_tag'

    id = Column(Integer, primary_key=True)
    t_id = Column(ForeignKey('c_a_tag.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    c_a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    c_a = relationship('CArticle', primaryjoin='CArticleTag.c_a_id == CArticle.a_id', backref='c_article_tags')
    t = relationship('CATag', primaryjoin='CArticleTag.t_id == CATag.a_id', backref='c_article_tags')



class CImage(Base):
    __tablename__ = 'c_images'

    i_id = Column(Integer, primary_key=True)
    i_name = Column(String(50))
    images = Column(LONGBLOB)
    link = Column(String(100))



class CMTag(Base):
    __tablename__ = 'c_m_tag'

    m_id = Column(Integer, primary_key=True)
    t_name = Column(String(50))



class CMusic(Base):
    __tablename__ = 'c_music'

    m_id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_name = Column(String(50))
    lyrics = Column(String(50))
    composition = Column(String(50))
    music = Column(LONGBLOB)
    isfree = Column(BIT(1))

    u = relationship('User', primaryjoin='CMusic.u_id == User.u_id', backref='c_musics')



class CMusicTag(Base):
    __tablename__ = 'c_music_tag'

    id = Column(Integer, primary_key=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    c_m_m_id = Column(ForeignKey('c_m_tag.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    c_m_m = relationship('CMTag', primaryjoin='CMusicTag.c_m_m_id == CMTag.m_id', backref='c_music_tags')
    m = relationship('CMusic', primaryjoin='CMusicTag.m_id == CMusic.m_id', backref='c_music_tags')



class Comment(Base):
    __tablename__ = 'comment'

    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    time = Column(String(20))
    content = Column(Text)
    id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    a = relationship('CArticle', primaryjoin='Comment.a_id == CArticle.a_id', backref='comments')
    m = relationship('CMusic', primaryjoin='Comment.m_id == CMusic.m_id', backref='comments')
    u = relationship('User', primaryjoin='Comment.u_id == User.u_id', backref='comments')



class FirstImage(Base):
    __tablename__ = 'first_images'

    img_id = Column(Integer, primary_key=True)
    link = Column(String(50))
    image = Column(LONGBLOB)



class FirstSentence(Base):
    __tablename__ = 'first_sentence'

    s_id = Column(Integer, primary_key=True)
    img_id = Column(ForeignKey('first_images.img_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    sentence = Column(Text)

    img = relationship('FirstImage', primaryjoin='FirstSentence.img_id == FirstImage.img_id', backref='first_sentences')



class MAbility(Base):
    __tablename__ = 'm_ability'

    m_id = Column(Integer, primary_key=True)
    m_user = Column(String(50))
    m_concent = Column(Text)
    m_notice = Column(Text)
    m_advertisement = Column(Text)
    m_msg = Column(Text)
    m_illegal_user = Column(String(20))
    m_illegal_content = Column(Text)



class MCharge2(Base):
    __tablename__ = 'm_charge2'

    id = Column(Integer, primary_key=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    gold = Column(Integer)

    m = relationship('CMusic', primaryjoin='MCharge2.m_id == CMusic.m_id', backref='m_charge2s')



class Manager(Base):
    __tablename__ = 'manager'

    m_id = Column(Integer, primary_key=True)
    m_a_m_id = Column(ForeignKey('m_ability.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    id = Column(ForeignKey('t_admin_level.id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_account = Column(String(30))
    m_pwd = Column(String(50))
    m_Email = Column(String(40))
    m_telephone = Column(String(30))
    m_set = Column(String(50))

    t_admin_level = relationship('TAdminLevel', primaryjoin='Manager.id == TAdminLevel.id', backref='managers')
    m_a_m = relationship('MAbility', primaryjoin='Manager.m_a_m_id == MAbility.m_id', backref='managers')



class TAdminLevel(Base):
    __tablename__ = 't_admin_level'

    id = Column(Integer, primary_key=True)
    lev = Column(Integer)
    category = Column(String(20))
    indetail = Column(Text)



class TAdvertising(Base):
    __tablename__ = 't_advertising'

    a_id = Column(Integer, primary_key=True)
    img_id = Column(ForeignKey('t_slidesshow.img_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    title = Column(String(100))
    text = Column(String(100))
    link = Column(String(100))

    img = relationship('TSlidesshow', primaryjoin='TAdvertising.img_id == TSlidesshow.img_id', backref='t_advertisings')



class TBuyVip(Base):
    __tablename__ = 't_buy_vip'

    id = Column(Integer, primary_key=True)
    v_id = Column(ForeignKey('t_vip_classify.v_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    open_time = Column(String(20), nullable=False)

    u = relationship('User', primaryjoin='TBuyVip.u_id == User.u_id', backref='t_buy_vips')
    v = relationship('TVipClassify', primaryjoin='TBuyVip.v_id == TVipClassify.v_id', backref='t_buy_vips')



class THaveread(Base):
    __tablename__ = 't_haveread'

    have_id = Column(Integer, primary_key=True)
    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    read_time = Column(String(20))

    a = relationship('CArticle', primaryjoin='THaveread.a_id == CArticle.a_id', backref='t_havereads')
    m = relationship('CMusic', primaryjoin='THaveread.m_id == CMusic.m_id', backref='t_havereads')
    u = relationship('User', primaryjoin='THaveread.u_id == User.u_id', backref='t_havereads')



class TLevelSuffer(Base):
    __tablename__ = 't_level_suffer'

    ID = Column(Integer, primary_key=True)
    grade = Column(Integer, nullable=False)
    experience = Column(Integer, nullable=False)



class TMessageFeedback(Base):
    __tablename__ = 't_message_feedback'

    id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    qq = Column(String(20))
    phone = Column(String(11))
    content = Column(Text)

    u = relationship('User', primaryjoin='TMessageFeedback.u_id == User.u_id', backref='t_message_feedbacks')



class TSlidesshow(Base):
    __tablename__ = 't_slidesshow'

    img_id = Column(Integer, primary_key=True)
    number = Column(Integer)
    image = Column(LONGBLOB)
    link = Column(String(100))



class TTask(Base):
    __tablename__ = 't_task'

    task_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    reward = Column(Integer, server_default=FetchedValue())
    description = Column(String(100))
    task_type = Column(String(20))



class TUserTask(Base):
    __tablename__ = 't_user_tasks'

    t_u_id = Column(Integer, primary_key=True)
    task_id = Column(ForeignKey('t_task.task_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    isfinish = Column(Integer)
    finish_time = Column(String(50))

    task = relationship('TTask', primaryjoin='TUserTask.task_id == TTask.task_id', backref='t_user_tasks')
    u = relationship('User', primaryjoin='TUserTask.u_id == User.u_id', backref='t_user_tasks')



class TUsermessage(Base):
    __tablename__ = 't_usermessage'

    title = Column(String(50))
    content = Column(Text)
    time = Column(String(16))
    id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    u = relationship('User', primaryjoin='TUsermessage.u_id == User.u_id', backref='t_usermessages')



class TVipClassify(Base):
    __tablename__ = 't_vip_classify'

    v_id = Column(Integer, primary_key=True)
    days = Column(Integer)
    price = Column(Integer)
    dis_days = Column(Integer)
    whether = Column(BIT(1), nullable=False)
    description = Column(Text)



class UCollection(Base):
    __tablename__ = 'u_collection'

    collection_id = Column(Integer, primary_key=True)
    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    datetime = Column(String(50))

    a = relationship('CArticle', primaryjoin='UCollection.a_id == CArticle.a_id', backref='u_collections')
    m = relationship('CMusic', primaryjoin='UCollection.m_id == CMusic.m_id', backref='u_collections')
    u = relationship('User', primaryjoin='UCollection.u_id == User.u_id', backref='u_collections')



class UDownload(Base):
    __tablename__ = 'u_download'

    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    d_id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    a = relationship('CArticle', primaryjoin='UDownload.a_id == CArticle.a_id', backref='u_downloads')
    m = relationship('CMusic', primaryjoin='UDownload.m_id == CMusic.m_id', backref='u_downloads')
    u = relationship('User', primaryjoin='UDownload.u_id == User.u_id', backref='u_downloads')



class UFabulou(Base):
    __tablename__ = 'u_fabulous'

    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    datatime = Column(String(20))
    id = Column(Integer, primary_key=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)

    a = relationship('CArticle', primaryjoin='UFabulou.a_id == CArticle.a_id', backref='u_fabulous')
    m = relationship('CMusic', primaryjoin='UFabulou.m_id == CMusic.m_id', backref='u_fabulous')
    u = relationship('User', primaryjoin='UFabulou.u_id == User.u_id', backref='u_fabulous')



class UGiveReward(Base):
    __tablename__ = 'u_give_reward'

    u_g_id = Column(Integer, primary_key=True)
    m_id = Column(ForeignKey('c_music.m_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    a_id = Column(ForeignKey('c_article.a_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    reward = Column(Integer)
    time = Column(String(16))

    a = relationship('CArticle', primaryjoin='UGiveReward.a_id == CArticle.a_id', backref='u_give_rewards')
    m = relationship('CMusic', primaryjoin='UGiveReward.m_id == CMusic.m_id', backref='u_give_rewards')
    u = relationship('User', primaryjoin='UGiveReward.u_id == User.u_id', backref='u_give_rewards')



class UPayClassify(Base):
    __tablename__ = 'u_pay_classify'

    pc_id = Column(Integer, primary_key=True)
    RMB = Column(Integer)
    number = Column(Integer)



class UPayrank(Base):
    __tablename__ = 'u_payrank'

    p_r_id = Column(Integer, primary_key=True)
    pc_id = Column(ForeignKey('u_pay_classify.pc_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    u_id = Column(ForeignKey('user.u_id', ondelete='RESTRICT', onupdate='RESTRICT'), index=True)
    time = Column(String(16))

    pc = relationship('UPayClassify', primaryjoin='UPayrank.pc_id == UPayClassify.pc_id', backref='u_payranks')
    u = relationship('User', primaryjoin='UPayrank.u_id == User.u_id', backref='u_payranks')



class User(Base):
    __tablename__ = 'user'

    u_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    phone = Column(String(11), nullable=False)
    vip_datetime = Column(String(20))
    image = Column(VARBINARY(100))
    balance = Column(Integer, server_default=FetchedValue())
    integral = Column(Integer, server_default=FetchedValue())
    pwd = Column(String(40))
    lev = Column(Integer, server_default=FetchedValue())
    experience = Column(Integer, server_default=FetchedValue())
    usedays = Column(Integer)
    v_level = Column(Integer)
    create_time = Column(String(20))
    isvip = Column(BIT(1))
