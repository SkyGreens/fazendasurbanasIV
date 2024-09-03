package com.skygreen.SkyGreen.Controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.skygreen.SkyGreen.entities.FuncionarioEntity;
import com.skygreen.SkyGreen.services.interfaces.IFuncionarioService;

import jakarta.transaction.Transactional;

@RestController
@RequestMapping("/funcionario")
public class FuncionarioRest {

    @Autowired
    private IFuncionarioService funcionarioService;

    @GetMapping("/listar")
    public ResponseEntity<List<FuncionarioEntity>> findAll(){

        return ResponseEntity.ok().body(funcionarioService.findAll());
    }

    @GetMapping(value = "/{id}")
    public ResponseEntity<FuncionarioEntity> findById(@PathVariable Integer id) {
        FuncionarioEntity result = funcionarioService.findById(id);
        return ResponseEntity.ok().body(result);
    }


    @Transactional
    @PostMapping("/adicionar")
    public ResponseEntity<FuncionarioEntity> add(@RequestBody FuncionarioEntity funcionarioEntity) {

        funcionarioEntity = funcionarioService.add(funcionarioEntity);
        return ResponseEntity.ok().body(funcionarioEntity);
    }

    @Transactional
    @DeleteMapping(value = "/delete/{id}")
    public ResponseEntity<Void> deleteUsuario(@PathVariable int id) {

        funcionarioService.delete(id);
        return ResponseEntity.ok().build();
    }

    @Transactional
    @PutMapping("/update")
    public ResponseEntity<FuncionarioEntity> updateUsuario(@RequestBody FuncionarioEntity funcionario) {

        FuncionarioEntity funcionarioAtualizado = funcionarioService.add(funcionario);
        return ResponseEntity.ok().body(funcionarioAtualizado);
    }

    @PostMapping("/login")
    public ResponseEntity<FuncionarioEntity> findByEmailAndSenha(@RequestParam String email, @RequestParam String senha) {
        FuncionarioEntity funcionario = funcionarioService.FindByEmailAndSenha(email, senha);
        
        return ResponseEntity.ok().body(funcionario);
    }
}
