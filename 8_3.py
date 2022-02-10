def type_logger(func):
   def type_logger_arg(*args):
      for i in args:
         print(f"test({i}: {type(i)})", sep="\n")
      return func(*args)
   return type_logger_arg


@type_logger
def args_sum(*args):
   return print(sum([i for i in args if isinstance(i, int) or isinstance(i, float)]))


args_sum(5, "trh", 45, 10.5)
