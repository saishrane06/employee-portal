INSERT INTO users (
    username,
    password
)
VALUES (
    'admin',
    'scrypt:32768:8:1$buuHY3EpdGudg8LU$6eea80ca683fda6442ebad9db5cac975f235997b4b12afcdafa0737f03bbd29fb1f5481e2ad5c8c63ba476b1f0875a0392861b71051a73cb5f91773975c08e8c'
)
ON CONFLICT (username)
DO NOTHING;