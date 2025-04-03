from typing import Callable, Any


class Event:
    """Classe que representa um evento para subscrição.

    Esta classe pode ser instanciada na forma atual ou pode ser especializada de modo a 
    a especificar a assinatura do handler aceite de modo mais estrito (usando type-hints) 
    e/ou para implementar outras customizações desejadas.
    """
    def __init__(self):
        self.__handlers = set()

    def add_handler(self, handler: Callable[[], None]) -> None:
        self.__handlers.add(handler)
    
    def remove_handler(self, handler: Callable) -> None:
        """Removes handler by object identity.
        
        If handler is not present, ignores request.
        """
        self.__handlers.discard(handler)
    
    def invoke(self, *args: Any, **kwargs: Any) -> None:
        for handler in self.__handlers:
            handler(*args, **kwargs)