package com.skygreen.SkyGreen.services;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestBody;

import com.skygreen.SkyGreen.entities.UsuarioEntity;
import com.skygreen.SkyGreen.repositories.UsuarioRepository;

import jakarta.persistence.EntityNotFoundException;

@Service
public class UsuarioServiceImpl implements UserDetailsService {

    @Autowired
    private UsuarioRepository repository;

    public List<UsuarioEntity> findAll() {
        return repository.findAll();
    }

    public UsuarioEntity add(UsuarioEntity usuario) {
        usuario = repository.save(usuario);
        return usuario;
    }

    public UsuarioEntity findById(Integer id) {
        return repository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("User not found with id " + id));
    }

    public void delete(Integer id) {
        repository.deleteById(id);
    }

    public UsuarioEntity updateUsuario(@RequestBody UsuarioEntity usuario) {

        usuario = repository.findById(usuario.getId()).orElse(null);

        usuario.setAtivo(usuario.getAtivo());
        usuario.setRole(usuario.getRole());
        usuario.setCpf(usuario.getCpf());
        usuario.setEmail(usuario.getEmail());
        usuario.setId(usuario.getId());
        usuario.setNome(usuario.getNome());
        usuario.setSenha(usuario.getSenha());

        usuario = repository.save(usuario);
        return usuario;
    }

    @Override
    public UserDetails loadUserByUsername(String cpf) throws UsernameNotFoundException {
        return repository.findUsuarioByCpf(cpf);
    }

}
