import re
from typing import List
from models import CommandType, RiskLevel, DetectedCommand
from patterns import DETECTION_PATTERNS

class SecurityLogic:
    def __init__(self, security_service):
        self.security_service = security_service
    
    def analyze_cli_request(self, content: str, command_type: CommandType) -> List[DetectedCommand]:
        try:
            detected = []
            
            # Get patterns for this command type
            patterns = DETECTION_PATTERNS.get(command_type, [])
            
            for pattern_info in patterns:
                pattern = pattern_info["pattern"]
                
                # Check if pattern matches content
                if re.search(pattern, content, re.IGNORECASE):
                    detected_command = DetectedCommand(
                        text=content,
                        command_type=command_type,
                        severity=pattern_info["severity"],
                        confidence=0.85,
                        pattern_matched=pattern,
                        context={"description": pattern_info["description"]}
                    )
                    detected.append(detected_command)
            
            return detected
            
        except Exception as e:
            print(f"failed for this reason {e}")
            return []
    
    def check_all_command_types(self, content: str) -> List[DetectedCommand]:
        """Check content against all command types"""
        all_detected = []
        
        for command_type in CommandType:
            detected = self.analyze_cli_request(content, command_type)
            all_detected.extend(detected)
        
        return all_detected
    
    def is_content_safe(self, content: str) -> bool:
        """Simple check if content is safe"""
        detected = self.check_all_command_types(content)
        
        # Block if any critical or high severity threats
        for threat in detected:
            if threat.severity in [RiskLevel.CRITICAL, RiskLevel.HIGH]:
                return False
        return True
    

"""    def role_priv(self, file_path, user_role, user_id):
        with open(file_path) as f: 
            content = f.read()
            detected = self.analyze_cli_request(content, CommandType.SYSTEM)
            
            critical_commands = []
            
            for cmd in detected:
                if cmd.severity == "CRITICAL" and user_role == "devops":
                    critical_commands.append({
                        f"user_{user_id}": cmd.text.strip()
                    })
            
            return critical_commands"""
                
            



        
        