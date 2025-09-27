def get_customer_address(cust_id:str):
  """ customer_id로 회원 주소를 조회하는 함수"""
  try:
    with SessionLocal() as _db:
      customer = _db.query(Customer).filter(Customer.cust_id == cust_id).first()

      if customer:
        return customer.cust_addr
      else:
        logger.info(f"No customer address for cust_id: {cust_id}")
        return None
  except Exception as e:
    logger.error(f"Unknown error while trying to fetch {cust_id}, and error: {e}")
