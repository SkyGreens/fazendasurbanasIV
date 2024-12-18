package com.skygreen.SkyGreen.repositories;

import java.util.Optional;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Repository;


import com.skygreen.SkyGreen.entities.UsuarioEntity;

@Repository
public interface UsuarioRepository extends JpaRepository<UsuarioEntity, Integer> {
    
   UserDetails findUsuarioByCpf(String cpf);
   Optional<UsuarioEntity> findByCpf(String cpf);
}
