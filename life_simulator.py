"""
多路径人生模拟引擎 - 核心模拟逻辑
"""
import random
from typing import List, Dict, Any
from models import (
    PersonProfile, LifePath, LifePathType, SimulationResult,
    TimelineNode, LifeEvent, ImpactLevel
)
from utils import (
    generate_id, calculate_success_probability, assess_risk_level,
    generate_timeline_milestones, format_comparison_matrix, format_date
)


class LifeSimulator:
    """人生模拟器"""

    def __init__(self):
        self.simulation_depth = 60  # 默认模拟60个月（5年）

    def create_simulation(
        self,
        profile: PersonProfile,
        num_paths: int = 5,
        years: int = 5
    ) -> SimulationResult:
        """
        创建多路径人生模拟

        Args:
            profile: 个人档案
            num_paths: 生成路径数量
            years: 模拟年限
        """
        simulation_id = generate_id("sim_")
        self.simulation_depth = years * 12

        # 生成多条人生路径
        paths = self._generate_diverse_paths(profile, num_paths)

        # 为每条路径进行深度模拟
        for path in paths:
            self._simulate_path_timeline(path, profile, years)

        # 生成对比分析
        comparison_matrix = format_comparison_matrix(paths)

        # 生成洞察和建议
        insights = self._generate_insights(paths, profile)
        recommendations = self._generate_recommendations(paths, profile)

        return SimulationResult(
            simulation_id=simulation_id,
            created_at=format_date(),
            person_profile=profile,
            paths=paths,
            comparison_matrix=comparison_matrix,
            recommendations=recommendations,
            insights=insights
        )

    def _generate_diverse_paths(
        self,
        profile: PersonProfile,
        num_paths: int
    ) -> List[LifePath]:
        """生成多样化的人生路径"""
        paths = []

        # 基于用户档案智能生成路径类型
        path_suggestions = self._suggest_path_types(profile)

        for i in range(min(num_paths, len(path_suggestions))):
            path_type, scenario = path_suggestions[i]
            path = self._create_path(profile, path_type, scenario, i + 1)
            paths.append(path)

        return paths

    def _suggest_path_types(
        self,
        profile: PersonProfile
    ) -> List[tuple]:
        """根据个人档案建议路径类型"""
        suggestions = []

        # 职业转换路径
        if "career_growth" in profile.goals or "change" in profile.current_career.lower():
            suggestions.append((
                LifePathType.CAREER_CHANGE,
                "转型到AI/技术领域"
            ))

        # 技能学习路径
        if len(profile.skills) < 5 or "learning" in str(profile.goals).lower():
            suggestions.append((
                LifePathType.SKILL_LEARNING,
                f"深度学习{profile.interests[0] if profile.interests else 'AI/编程'}"
            ))

        # 创业路径
        if profile.age < 40 and "entrepreneur" in str(profile.goals).lower():
            suggestions.append((
                LifePathType.ENTREPRENEURSHIP,
                "基于技能创业"
            ))

        # 健康健身路径
        if "health" in str(profile.goals).lower() or profile.health_status != "excellent":
            suggestions.append((
                LifePathType.HEALTH_FITNESS,
                "系统性健身与健康管理"
            ))

        # 教育深造路径
        if profile.age < 35 and "education" in str(profile.goals).lower():
            suggestions.append((
                LifePathType.EDUCATION,
                "攻读高级学位或专业认证"
            ))

        # 如果建议不足，添加通用路径
        generic_paths = [
            (LifePathType.LIFESTYLE_CHANGE, "优化生活节奏与时间管理"),
            (LifePathType.RELATIONSHIP, "发展深度人际关系"),
            (LifePathType.RELOCATION, "迁移到更好的城市环境")
        ]

        for gp in generic_paths:
            if len(suggestions) < 5:
                suggestions.append(gp)

        return suggestions[:5]

    def _create_path(
        self,
        profile: PersonProfile,
        path_type: LifePathType,
        scenario: str,
        index: int
    ) -> LifePath:
        """创建单条人生路径"""
        path_id = generate_id(f"path_{index}_")

        # 计算成功概率
        success_prob = calculate_success_probability(
            skills=profile.skills,
            resources={"financial": profile.financial_status, "network": True},
            challenges=profile.constraints,
            time_investment=self.simulation_depth // 12
        )

        # 评估风险等级
        risk_level = assess_risk_level(
            path_type=path_type.value,
            financial_impact="medium",
            time_commitment=self.simulation_depth // 12,
            reversibility="medium"
        )

        # 生成关键因素
        key_factors = self._identify_key_factors(path_type, profile)

        return LifePath(
            path_id=path_id,
            path_type=path_type,
            title=f"路径{index}: {scenario}",
            description=self._generate_path_description(path_type, scenario, profile),
            initial_decision=f"决定：{scenario}",
            success_probability=success_prob,
            risk_level=risk_level,
            key_factors=key_factors
        )

    def _simulate_path_timeline(
        self,
        path: LifePath,
        profile: PersonProfile,
        years: int
    ) -> None:
        """模拟路径时间线"""
        milestones = generate_timeline_milestones(years, path.path_type.value)

        # 为每年生成时间节点
        for year in range(years):
            for quarter in range(4):
                month = year * 12 + quarter * 3
                node = self._generate_timeline_node(
                    year, quarter * 3, path, profile, milestones
                )
                path.timeline.append(node)

        # 生成最终状态
        path.final_state = self._generate_final_state(path, profile, years)

    def _generate_timeline_node(
        self,
        year: int,
        month: int,
        path: LifePath,
        profile: PersonProfile,
        milestones: List[Dict[str, Any]]
    ) -> TimelineNode:
        """生成时间线节点"""
        current_month = year * 12 + month

        # 查找该时间点的里程碑
        milestone_events = [
            m for m in milestones
            if abs(m["month"] - current_month) <= 1
        ]

        # 生成事件
        events = []
        for milestone in milestone_events:
            event = LifeEvent(
                timestamp=f"Y{year}M{month}",
                event_type=path.path_type.value,
                description=milestone["title"],
                impact_level=ImpactLevel.HIGH,
                consequences=[
                    f"完成度达到 {milestone['completion_rate']*100:.0f}%",
                    f"获得相关经验和能力提升"
                ],
                skills_gained=self._generate_skills_for_milestone(milestone["title"])
            )
            events.append(event)

        # 随机生成一些小事件
        if random.random() > 0.7:
            minor_event = self._generate_random_event(path.path_type, year, month)
            events.append(minor_event)

        # 生成状态快照
        state_snapshot = {
            "career_level": min(10, 5 + current_month // 6),
            "skill_proficiency": min(100, 30 + current_month * 1.2),
            "network_size": 50 + current_month * 5,
            "financial_growth": 1.0 + current_month * 0.05,
            "satisfaction": min(10, 6 + random.uniform(0, 4)),
            "stress_level": max(1, 5 - current_month * 0.05)
        }

        # 成就和挑战
        achievements = self._generate_achievements(current_month, path)
        challenges = self._generate_challenges(current_month, path)

        # 成长指标
        growth_metrics = {
            "技能成长": min(1.0, current_month / 60 * random.uniform(0.8, 1.0)),
            "经验累积": min(1.0, current_month / 60 * random.uniform(0.7, 1.0)),
            "人脉扩展": min(1.0, current_month / 60 * random.uniform(0.6, 1.0)),
            "财务改善": min(1.0, current_month / 60 * random.uniform(0.5, 0.9))
        }

        return TimelineNode(
            year=year,
            month=month,
            state_snapshot=state_snapshot,
            major_events=events,
            achievements=achievements,
            challenges=challenges,
            growth_metrics=growth_metrics
        )

    def _generate_final_state(
        self,
        path: LifePath,
        profile: PersonProfile,
        years: int
    ) -> Dict[str, Any]:
        """生成最终状态"""
        success_multiplier = path.success_probability

        return {
            "career_position": self._project_career(path.path_type, years, success_multiplier),
            "skill_mastery": self._project_skills(profile.skills, years, success_multiplier),
            "financial_status": self._project_finances(profile.financial_status, years, success_multiplier),
            "health_wellness": self._project_health(path.path_type, years),
            "relationship_quality": self._project_relationships(path.path_type, years),
            "life_satisfaction": min(10, 6 + years * success_multiplier),
            "achievements": self._project_achievements(path, years),
            "regrets": self._project_regrets(path, years),
            "next_opportunities": self._project_opportunities(path, years)
        }

    def _project_career(self, path_type: LifePathType, years: int, success: float) -> str:
        """预测职业发展"""
        career_map = {
            LifePathType.CAREER_CHANGE: f"成功转型，担任{['初级', '中级', '高级'][min(2, years//2)]}职位",
            LifePathType.ENTREPRENEURSHIP: f"创业{['起步', '稳定', '成功'][min(2, years//2)]}阶段",
            LifePathType.SKILL_LEARNING: f"成为该领域{['入门', '熟练', '专家'][min(2, years//2)]}",
            LifePathType.EDUCATION: f"获得{['在读', '毕业', '应用'][min(2, years//2)]}状态"
        }
        return career_map.get(path_type, f"在当前领域发展到更高层次")

    def _project_skills(self, current_skills: List[str], years: int, success: float) -> Dict[str, float]:
        """预测技能发展"""
        skill_projection = {}
        for skill in current_skills:
            growth = min(10, 5 + years * success * random.uniform(0.5, 1.0))
            skill_projection[skill] = growth

        # 添加新技能
        new_skills_count = int(years * success * 2)
        for i in range(new_skills_count):
            skill_projection[f"新技能_{i+1}"] = random.uniform(3, 7)

        return skill_projection

    def _project_finances(self, current_status: str, years: int, success: float) -> str:
        """预测财务状况"""
        status_map = {"low": 0, "medium": 1, "high": 2}
        current_level = status_map.get(current_status.lower(), 0)
        growth = int(years * success * 0.5)
        final_level = min(2, current_level + growth)
        return ["稳定但有限", "舒适且有储蓄", "富足且有投资"][final_level]

    def _project_health(self, path_type: LifePathType, years: int) -> str:
        """预测健康状况"""
        if path_type == LifePathType.HEALTH_FITNESS:
            return "显著改善，达到最佳状态"
        elif path_type == LifePathType.ENTREPRENEURSHIP:
            return "压力较大，需要注意平衡"
        return "保持良好，有规律的生活习惯"

    def _project_relationships(self, path_type: LifePathType, years: int) -> str:
        """预测人际关系"""
        if path_type == LifePathType.RELATIONSHIP:
            return "深度关系网络，高质量连接"
        elif path_type in [LifePathType.ENTREPRENEURSHIP, LifePathType.EDUCATION]:
            return "专业人脉扩展，合作关系增强"
        return "稳定的社交圈，质量提升"

    def _project_achievements(self, path: LifePath, years: int) -> List[str]:
        """预测成就"""
        achievements = [
            f"完成{path.path_type.value}的主要目标",
            f"积累{years}年相关经验",
            f"建立专业声誉和影响力"
        ]
        if path.success_probability > 0.7:
            achievements.append("超预期完成，获得行业认可")
        return achievements

    def _project_regrets(self, path: LifePath, years: int) -> List[str]:
        """预测可能的遗憾"""
        regrets = []
        if path.risk_level == "高风险":
            regrets.append("过程中经历了较大压力")
        if path.success_probability < 0.5:
            regrets.append("某些目标未能完全达成")
        if not regrets:
            regrets.append("整体满意，遗憾较少")
        return regrets

    def _project_opportunities(self, path: LifePath, years: int) -> List[str]:
        """预测未来机会"""
        return [
            f"基于{path.path_type.value}经验的进阶机会",
            "横向拓展到相关领域",
            "指导他人或成为意见领袖",
            "更大的平台和资源"
        ]

    def _generate_path_description(
        self,
        path_type: LifePathType,
        scenario: str,
        profile: PersonProfile
    ) -> str:
        """生成路径描述"""
        return f"""
这条路径探索了{scenario}的可能性。
基于你当前的{profile.current_career}背景和{', '.join(profile.skills[:3])}等技能，
这个方向将带来{path_type.value}方面的深度发展。
通过系统性的规划和执行，预计将在多个维度实现突破。
        """.strip()

    def _identify_key_factors(
        self,
        path_type: LifePathType,
        profile: PersonProfile
    ) -> List[str]:
        """识别关键因素"""
        factors = [
            f"当前技能基础: {', '.join(profile.skills[:3])}",
            f"年龄优势: {profile.age}岁正处于发展期",
            f"个性特质: {', '.join(profile.personality_traits[:2]) if profile.personality_traits else '适应性强'}"
        ]

        if path_type == LifePathType.ENTREPRENEURSHIP:
            factors.extend([
                "市场机会窗口",
                "风险承受能力",
                "资源整合能力"
            ])
        elif path_type == LifePathType.SKILL_LEARNING:
            factors.extend([
                "学习投入时间",
                "实践机会",
                "导师指导"
            ])

        return factors

    def _generate_skills_for_milestone(self, milestone_title: str) -> List[str]:
        """为里程碑生成技能"""
        skill_keywords = {
            "研究": ["分析能力", "信息收集"],
            "认证": ["专业知识", "考试技巧"],
            "人脉": ["社交能力", "关系维护"],
            "面试": ["沟通能力", "自我展示"],
            "团队": ["协作能力", "领导力"],
            "客户": ["销售技巧", "客户服务"],
            "项目": ["项目管理", "执行力"]
        }

        skills = []
        for keyword, skill_list in skill_keywords.items():
            if keyword in milestone_title:
                skills.extend(skill_list)

        return skills[:2] if skills else ["经验积累"]

    def _generate_random_event(
        self,
        path_type: LifePathType,
        year: int,
        month: int
    ) -> LifeEvent:
        """生成随机事件"""
        event_pool = [
            "遇到关键导师",
            "参加重要会议",
            "获得意外机会",
            "克服重大挑战",
            "建立重要合作",
            "完成关键项目"
        ]

        return LifeEvent(
            timestamp=f"Y{year}M{month}",
            event_type="随机事件",
            description=random.choice(event_pool),
            impact_level=random.choice([ImpactLevel.MEDIUM, ImpactLevel.HIGH]),
            consequences=[f"为{path_type.value}带来新的动力"]
        )

    def _generate_achievements(self, month: int, path: LifePath) -> List[str]:
        """生成成就"""
        if month % 12 == 0 and month > 0:
            return [f"完成第{month//12}年度目标"]
        elif month % 6 == 0:
            return [f"半年度里程碑达成"]
        return []

    def _generate_challenges(self, month: int, path: LifePath) -> List[str]:
        """生成挑战"""
        challenges_pool = [
            "时间管理压力",
            "技能瓶颈突破",
            "资源限制",
            "心理适应",
            "外部竞争"
        ]

        if month > 0 and month % 8 == 0:
            return [random.choice(challenges_pool)]
        return []

    def _generate_insights(
        self,
        paths: List[LifePath],
        profile: PersonProfile
    ) -> List[str]:
        """生成洞察"""
        insights = []

        # 比较成功概率
        best_path = max(paths, key=lambda p: p.success_probability)
        insights.append(
            f"'{best_path.title}' 具有最高成功概率 ({best_path.success_probability:.1%})，"
            f"这与你的{profile.current_career}背景高度契合"
        )

        # 风险分析
        high_risk_paths = [p for p in paths if p.risk_level == "高风险"]
        if high_risk_paths:
            insights.append(
                f"有 {len(high_risk_paths)} 条路径属于高风险，但可能带来突破性成长"
            )

        # 时间投入
        insights.append(
            f"所有路径都需要持续{self.simulation_depth//12}年的专注投入，"
            "前18个月是关键建立期"
        )

        # 个性化洞察
        if profile.age < 30:
            insights.append("年龄优势明显，试错成本较低，可以考虑更激进的路径")
        elif profile.age > 40:
            insights.append("经验丰富，建议选择能够放大现有优势的路径")

        return insights

    def _generate_recommendations(
        self,
        paths: List[LifePath],
        profile: PersonProfile
    ) -> List[str]:
        """生成建议"""
        recommendations = []

        # 基于成功概率推荐
        sorted_paths = sorted(paths, key=lambda p: p.success_probability, reverse=True)
        recommendations.append(
            f"优先考虑: {sorted_paths[0].title} - "
            f"成功率高且风险可控"
        )

        # 基于目标推荐
        if "快速成长" in str(profile.goals):
            skill_paths = [p for p in paths if p.path_type == LifePathType.SKILL_LEARNING]
            if skill_paths:
                recommendations.append(
                    f"对齐目标: {skill_paths[0].title} - "
                    "直接对应你的成长需求"
                )

        # 组合建议
        recommendations.append(
            "可以考虑组合策略: 主路径 + 辅助路径并行，"
            "如职业发展 + 健康管理"
        )

        # 行动建议
        recommendations.append(
            "建议先进行3个月的小规模试验，"
            "验证假设后再全力投入"
        )

        return recommendations
