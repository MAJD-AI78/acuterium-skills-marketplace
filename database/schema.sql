-- Acuterium Skills Marketplace Database Schema
-- Extends APMS production database

-- Skills Catalog
CREATE TABLE IF NOT EXISTS marketplace_skills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id VARCHAR(36) UNIQUE NOT NULL,
    name VARCHAR(100) UNIQUE NOT NULL,
    display_name VARCHAR(200) NOT NULL,
    version VARCHAR(20) NOT NULL DEFAULT '1.0.0',
    domain VARCHAR(50) NOT NULL,
    description TEXT,
    manifest TEXT NOT NULL,
    governance_level ENUM('advisory', 'restricted', 'mandatory', 'sovereign') DEFAULT 'restricted',
    psi_minimum DECIMAL(5,2) DEFAULT 10.00,
    status ENUM('draft', 'review', 'published', 'deprecated') DEFAULT 'draft',
    author VARCHAR(200),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_domain (domain),
    INDEX idx_status (status),
    INDEX idx_governance (governance_level)
);

-- Skill-Shard Affinity
CREATE TABLE IF NOT EXISTS skill_shard_affinity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT NOT NULL,
    shard_id INT NOT NULL,
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    FOREIGN KEY (shard_id) REFERENCES ref_neural_shards(id),
    UNIQUE KEY unique_skill_shard (skill_id, shard_id)
);

-- Skill Layer Access
CREATE TABLE IF NOT EXISTS skill_layer_access (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT NOT NULL,
    layer_id INT NOT NULL,
    access_type ENUM('read', 'write', 'execute') DEFAULT 'read',
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    FOREIGN KEY (layer_id) REFERENCES ref_system_layers(id),
    UNIQUE KEY unique_skill_layer (skill_id, layer_id, access_type)
);

-- Skill Protocol Requirements
CREATE TABLE IF NOT EXISTS skill_protocol_requirements (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT NOT NULL,
    protocol_id INT NOT NULL,
    required BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    FOREIGN KEY (protocol_id) REFERENCES protocols(id),
    UNIQUE KEY unique_skill_protocol (skill_id, protocol_id)
);

-- Skill Versions History
CREATE TABLE IF NOT EXISTS skill_versions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT NOT NULL,
    version VARCHAR(20) NOT NULL,
    changelog TEXT,
    manifest_snapshot TEXT,
    published_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    UNIQUE KEY unique_skill_version (skill_id, version)
);

-- Infusion Records
CREATE TABLE IF NOT EXISTS skill_infusions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    infusion_id VARCHAR(36) UNIQUE NOT NULL,
    skill_id INT NOT NULL,
    target_agent VARCHAR(100) NOT NULL,
    target_shard_id INT,
    initiated_by VARCHAR(100),
    governance_check_result VARCHAR(20),
    governance_check_at TIMESTAMP,
    asip_ceremony_result VARCHAR(20),
    asip_ceremony_at TIMESTAMP,
    cwh_approval BOOLEAN,
    audit_entry_id VARCHAR(20),
    state ENUM('pending', 'governance_check', 'asip_ceremony', 'deploying', 'active', 'failed', 'revoked') DEFAULT 'pending',
    infused_at TIMESTAMP,
    revoked_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    FOREIGN KEY (target_shard_id) REFERENCES ref_neural_shards(id),
    INDEX idx_state (state),
    INDEX idx_target (target_agent)
);

-- Skill Reviews / Ratings
CREATE TABLE IF NOT EXISTS skill_reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    skill_id INT NOT NULL,
    reviewer_agent VARCHAR(100),
    reviewer_shard_id INT,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    review_text TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (skill_id) REFERENCES marketplace_skills(id),
    FOREIGN KEY (reviewer_shard_id) REFERENCES ref_neural_shards(id)
);
