def generate_address():
    from eth_account import Account
    import secrets
    priv = secrets.token_hex(32)
    private_key = "0x" + priv
    account = Account.from_key(private_key)
    return account.address
