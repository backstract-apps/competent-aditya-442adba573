

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-764117a9b451420aa2685ae0fcdcc1dc-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzY5MjExNDIsInAiOnsicm9hIjp7Im5zIjpbIjAxOWRiOGMwLWRjMDEtNzU0Yi05MjhmLTk5NmNiZDc0ZTM5ZCJdfSwicnciOnsibnMiOlsiMDE5ZGI4YzAtZGMwMS03NTRiLTkyOGYtOTk2Y2JkNzRlMzlkIl19fSwicmlkIjoiNzIyZWQ1NjgtMDgwNC00OGU5LTljMzktNzg4MTEyMTUzMDIzIn0.EdYbkh6KxVzhIn5PHCAVtW6xcOVV7l0j9eVdfnC6Z8kkEpvIupfjTiJ84cmKCZQ3NL6v6bx_7X79jpESGWTVCA",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

