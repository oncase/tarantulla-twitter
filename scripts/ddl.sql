CREATE TABLE <yourSCHEMA>.<yourTABLE>
(
  twitter_id character varying(50) PRIMARY KEY,
  timestamp_twitter timestamp without time zone,
  created_at character varying(50),
  publisher_twitter character varying(50),
  publisher_name character varying(50),
  tweet_content character varying(400),
  dim_hashtag character varying(100),
  link_tweet character varying(100),
  rts double precision,
  favs double precision,
  engagement double precision
)
