from django.db import connection

def get_all_posts(page, limit):
    offset = (page - 1) * limit  # OFFSET 계산

    sql = """
        SELECT p.post_id, p.title, p.contents, p.like_cnt, p.comment_cnt, p.view_cnt, 
               p.created_at, p.updated_at,
               u.user_id, u.nickname, u.email, u.image_url 
        FROM posts p
        JOIN users u ON p.user_id = u.user_id
        WHERE p.is_deleted = FALSE AND u.is_deleted = FALSE
        ORDER BY p.created_at DESC
        LIMIT %s OFFSET %s
    """

    with connection.cursor() as cursor:
        cursor.execute(sql, [limit, offset])
        rows = cursor.fetchall()

    posts = [
        {
            "post_id": row[0],
            "title": row[1],
            "content": row[2],
            "like_cnt": row[3],
            "comment_cnt": row[4],
            "view_cnt": row[5],
            "created_at": row[6],
            "updated_at": row[7],
            "author": {
                "user_id": row[8],
                "nickname": row[9],
                "email": row[10],
                "image_url": row[11],
            }
        }
        for row in rows
    ]

    return posts