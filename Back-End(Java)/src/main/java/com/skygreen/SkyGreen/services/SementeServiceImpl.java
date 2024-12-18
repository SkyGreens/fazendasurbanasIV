package com.skygreen.SkyGreen.services;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.skygreen.SkyGreen.entities.SementeEntity;
import com.skygreen.SkyGreen.repositories.SementeRepository;
import com.skygreen.SkyGreen.services.interfaces.ISementeService;

import jakarta.persistence.EntityNotFoundException;

@Service
public class SementeServiceImpl implements ISementeService {

    @Autowired
    private SementeRepository sementeRepository;

    @Override
    public List<SementeEntity> findAll() {
        return sementeRepository.findAll();
    }

    @Override
    public SementeEntity sementeById(Integer id) {
        return sementeRepository.findById(id)
                .orElseThrow(() -> new EntityNotFoundException("Semente não encontrada"));
    }

    @Override
    public SementeEntity criarSemente(SementeEntity semente) {
        return sementeRepository.save(semente);
    }

    public Optional<SementeEntity> findById(Integer sementeId) {
        
        return sementeRepository.findById(sementeId);
    }

    @Override
    public void delete(Integer id) {
        sementeRepository.deleteById(id);
    }
}
