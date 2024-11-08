package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.PedidoCompraEntity;
import com.skygreen.SkyGreen.services.interfaces.IPedidoCompraService;

@RestController
@RequestMapping("/compras")
public class PedidoCompraController {

    @Autowired
    private IPedidoCompraService pedidoCompraService;

    @PostMapping("/pedido")
    public PedidoCompraEntity criarPedido(@RequestBody PedidoCompraEntity pedidoCompra) {
        return pedidoCompraService.criarPedido(pedidoCompra);
    }

    @GetMapping("/")
    public List<PedidoCompraEntity> getPedidos() {
        return pedidoCompraService.getPedidos();
    }
}
