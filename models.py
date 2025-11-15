"""
数据模型定义 - 人生仿真引擎
"""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime
from enum import Enum


class LifePathType(Enum):
    """人生路径类型"""
    CAREER_CHANGE = "职业转换"
    EDUCATION = "教育深造"
    ENTREPRENEURSHIP = "创业"
    RELATIONSHIP = "感情发展"
    HEALTH_FITNESS = "健康健身"
    SKILL_LEARNING = "技能学习"
    LIFESTYLE_CHANGE = "生活方式改变"
    RELOCATION = "地理迁移"


class ImpactLevel(Enum):
    """影响程度"""
    CRITICAL = "关键性"
    HIGH = "高"
    MEDIUM = "中等"
    LOW = "低"


@dataclass
class PersonProfile:
    """个人档案"""
    name: str
    age: int
    current_career: str
    education: str
    skills: List[str] = field(default_factory=list)
    interests: List[str] = field(default_factory=list)
    financial_status: str = ""
    health_status: str = ""
    relationship_status: str = ""
    personality_traits: List[str] = field(default_factory=list)
    goals: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)


@dataclass
class LifeEvent:
    """人生事件"""
    timestamp: str
    event_type: str
    description: str
    impact_level: ImpactLevel
    consequences: List[str] = field(default_factory=list)
    skills_gained: List[str] = field(default_factory=list)
    resources_changed: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TimelineNode:
    """时间线节点"""
    year: int
    month: int
    state_snapshot: Dict[str, Any]
    major_events: List[LifeEvent] = field(default_factory=list)
    achievements: List[str] = field(default_factory=list)
    challenges: List[str] = field(default_factory=list)
    growth_metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class LifePath:
    """人生路径"""
    path_id: str
    path_type: LifePathType
    title: str
    description: str
    initial_decision: str
    timeline: List[TimelineNode] = field(default_factory=list)
    final_state: Dict[str, Any] = field(default_factory=dict)
    success_probability: float = 0.0
    risk_level: str = "中等"
    key_factors: List[str] = field(default_factory=list)
    alternative_branches: List[str] = field(default_factory=list)


@dataclass
class SimulationResult:
    """模拟结果"""
    simulation_id: str
    created_at: str
    person_profile: PersonProfile
    paths: List[LifePath]
    comparison_matrix: Dict[str, Any] = field(default_factory=dict)
    recommendations: List[str] = field(default_factory=list)
    insights: List[str] = field(default_factory=list)


@dataclass
class KnowledgeNode:
    """知识节点"""
    node_id: str
    title: str
    level: int
    content: str
    concepts: List[str] = field(default_factory=list)
    connections: List[str] = field(default_factory=list)
    importance_score: float = 0.0


@dataclass
class KnowledgeGraph:
    """知识图谱"""
    topic: str
    nodes: List[KnowledgeNode] = field(default_factory=list)
    max_depth: int = 20
    total_concepts: int = 0
    framework: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DailyReport:
    """每日报告"""
    date: str
    mood_analysis: Dict[str, Any]
    input_summary: Dict[str, List[str]]
    brain_summary: str
    growth_insights: List[str] = field(default_factory=list)
    tomorrow_suggestions: List[str] = field(default_factory=list)
    metrics: Dict[str, float] = field(default_factory=dict)


@dataclass
class LifePlan:
    """生活规划"""
    plan_type: str
    title: str
    duration_months: int
    phases: List[Dict[str, Any]] = field(default_factory=list)
    milestones: List[str] = field(default_factory=list)
    habit_system: Dict[str, Any] = field(default_factory=dict)
    resources_needed: List[str] = field(default_factory=list)
    success_metrics: List[str] = field(default_factory=list)
