"""
工具函数 - 人生仿真引擎
"""
import random
import json
from datetime import datetime, timedelta
from typing import List, Dict, Any


def generate_id(prefix: str = "") -> str:
    """生成唯一ID"""
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    random_suffix = random.randint(1000, 9999)
    return f"{prefix}{timestamp}_{random_suffix}" if prefix else f"{timestamp}_{random_suffix}"


def calculate_success_probability(
    skills: List[str],
    resources: Dict[str, Any],
    challenges: List[str],
    time_investment: int
) -> float:
    """计算成功概率"""
    base_probability = 0.5

    # 技能加成
    skill_bonus = min(len(skills) * 0.05, 0.2)

    # 资源加成
    resource_bonus = 0.1 if resources.get("financial", "low") in ["medium", "high"] else 0
    resource_bonus += 0.1 if resources.get("network", False) else 0

    # 挑战惩罚
    challenge_penalty = min(len(challenges) * 0.03, 0.15)

    # 时间投入加成
    time_bonus = min(time_investment / 12 * 0.1, 0.15)

    probability = base_probability + skill_bonus + resource_bonus + time_bonus - challenge_penalty
    return max(0.1, min(0.95, probability))


def assess_risk_level(
    path_type: str,
    financial_impact: str,
    time_commitment: int,
    reversibility: str
) -> str:
    """评估风险等级"""
    risk_score = 0

    # 路径类型风险
    high_risk_types = ["创业", "职业转换", "地理迁移"]
    if path_type in high_risk_types:
        risk_score += 2

    # 财务影响
    if financial_impact == "high":
        risk_score += 3
    elif financial_impact == "medium":
        risk_score += 1

    # 时间承诺
    if time_commitment > 24:
        risk_score += 2
    elif time_commitment > 12:
        risk_score += 1

    # 可逆性
    if reversibility == "low":
        risk_score += 2

    if risk_score >= 6:
        return "高风险"
    elif risk_score >= 3:
        return "中等风险"
    else:
        return "低风险"


def generate_timeline_milestones(
    duration_years: int,
    path_type: str
) -> List[Dict[str, Any]]:
    """生成时间线里程碑"""
    milestones = []
    months = duration_years * 12

    # 不同路径类型的典型里程碑
    milestone_templates = {
        "职业转换": [
            "决定转型并开始研究",
            "获得第一个相关技能认证",
            "建立行业人脉网络",
            "获得第一个面试机会",
            "成功转型并适应新角色"
        ],
        "创业": [
            "完成商业计划",
            "组建核心团队",
            "获得第一个客户",
            "实现收支平衡",
            "业务规模化扩展"
        ],
        "技能学习": [
            "掌握基础知识",
            "完成第一个实践项目",
            "达到中级水平",
            "获得认证或作品",
            "成为该领域专家"
        ],
        "健康健身": [
            "建立运动习惯",
            "看到初步身体变化",
            "突破体能瓶颈",
            "达到目标体型",
            "保持健康生活方式"
        ]
    }

    templates = milestone_templates.get(path_type, [
        "启动阶段",
        "初步进展",
        "中期突破",
        "成果显现",
        "目标达成"
    ])

    for i, template in enumerate(templates):
        month = int((i + 1) * months / len(templates))
        milestones.append({
            "month": month,
            "title": template,
            "completion_rate": (i + 1) / len(templates)
        })

    return milestones


def format_comparison_matrix(paths: List[Any]) -> Dict[str, Any]:
    """格式化对比矩阵"""
    comparison = {
        "criteria": [
            "成功概率",
            "风险等级",
            "时间投入",
            "财务要求",
            "个人成长",
            "生活质量",
            "社会价值"
        ],
        "paths": []
    }

    for path in paths:
        path_comparison = {
            "path_id": path.path_id,
            "title": path.title,
            "scores": generate_path_scores(path)
        }
        comparison["paths"].append(path_comparison)

    return comparison


def generate_path_scores(path: Any) -> Dict[str, float]:
    """生成路径评分"""
    # 这里使用启发式评分，实际应用中可以更复杂
    return {
        "成功概率": path.success_probability,
        "风险等级": {"低风险": 0.8, "中等风险": 0.5, "高风险": 0.3}.get(path.risk_level, 0.5),
        "时间投入": random.uniform(0.4, 0.9),
        "财务要求": random.uniform(0.3, 0.8),
        "个人成长": random.uniform(0.6, 0.95),
        "生活质量": random.uniform(0.5, 0.9),
        "社会价值": random.uniform(0.4, 0.85)
    }


def save_to_json(data: Any, filename: str) -> None:
    """保存数据到JSON文件"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=str)


def load_from_json(filename: str) -> Any:
    """从JSON文件加载数据"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None


def format_date(days_offset: int = 0) -> str:
    """格式化日期"""
    date = datetime.now() + timedelta(days=days_offset)
    return date.strftime("%Y-%m-%d")


def calculate_growth_rate(
    initial_value: float,
    final_value: float,
    months: int
) -> float:
    """计算增长率"""
    if initial_value == 0:
        return 0
    total_growth = (final_value - initial_value) / initial_value
    monthly_rate = total_growth / months if months > 0 else 0
    return monthly_rate


def generate_color_tag(score: float) -> str:
    """根据分数生成颜色标记（用于终端显示）"""
    if score >= 0.8:
        return "🟢"  # 绿色 - 优秀
    elif score >= 0.6:
        return "🟡"  # 黄色 - 良好
    elif score >= 0.4:
        return "🟠"  # 橙色 - 一般
    else:
        return "🔴"  # 红色 - 需要改进
