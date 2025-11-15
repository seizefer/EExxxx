"""
生活规划师 - 未来规划、习惯系统、自我提升方案
"""
from typing import List, Dict, Any, Optional
from models import PersonProfile, LifePlan
from utils import generate_id, format_date
import random


class LifePlanner:
    """生活规划师"""

    def __init__(self):
        self.plan_templates = self._init_plan_templates()

    def _init_plan_templates(self) -> Dict[str, Any]:
        """初始化规划模板"""
        return {
            "habit_building": {
                "duration": 90,
                "phases": ["启动期", "巩固期", "内化期"],
                "success_rate": 0.65
            },
            "skill_acquisition": {
                "duration": 180,
                "phases": ["基础期", "实践期", "精通期"],
                "success_rate": 0.70
            },
            "career_transition": {
                "duration": 365,
                "phases": ["准备期", "过渡期", "稳定期", "发展期"],
                "success_rate": 0.60
            },
            "health_transformation": {
                "duration": 180,
                "phases": ["适应期", "突破期", "保持期"],
                "success_rate": 0.75
            }
        }

    def create_future_plan(
        self,
        profile: PersonProfile,
        plan_type: str,
        goal: str,
        duration_months: int = 12
    ) -> LifePlan:
        """
        创建未来规划

        Args:
            profile: 个人档案
            plan_type: 规划类型（career/skill/health/lifestyle）
            goal: 具体目标
            duration_months: 持续时间（月）
        """
        plan = LifePlan(
            plan_type=plan_type,
            title=f"{plan_type}规划: {goal}",
            duration_months=duration_months
        )

        # 生成阶段性计划
        plan.phases = self._generate_phases(plan_type, duration_months, goal)

        # 生成里程碑
        plan.milestones = self._generate_milestones(plan_type, duration_months)

        # 设计习惯系统
        plan.habit_system = self._design_habit_system(plan_type, profile)

        # 识别所需资源
        plan.resources_needed = self._identify_resources(plan_type, goal)

        # 定义成功指标
        plan.success_metrics = self._define_success_metrics(plan_type, goal)

        return plan

    def create_habit_system(
        self,
        profile: PersonProfile,
        target_area: str
    ) -> Dict[str, Any]:
        """
        创建习惯系统

        Args:
            target_area: 目标领域（如：productivity, health, learning）
        """
        habit_system = {
            "target_area": target_area,
            "core_habits": self._define_core_habits(target_area),
            "trigger_design": self._design_triggers(target_area),
            "reward_system": self._design_rewards(target_area),
            "tracking_method": self._design_tracking(target_area),
            "accountability": self._design_accountability(target_area),
            "progression_plan": self._design_progression(target_area)
        }

        return habit_system

    def create_self_improvement_plan(
        self,
        profile: PersonProfile,
        focus_areas: List[str]
    ) -> Dict[str, Any]:
        """
        创建自我提升方案

        Args:
            focus_areas: 关注领域列表
        """
        improvement_plan = {
            "assessment": self._assess_current_state(profile, focus_areas),
            "growth_roadmap": {},
            "daily_practices": [],
            "weekly_reviews": [],
            "monthly_goals": [],
            "learning_resources": {}
        }

        # 为每个领域创建成长路线图
        for area in focus_areas:
            improvement_plan["growth_roadmap"][area] = self._create_growth_roadmap(area, profile)

        # 设计日常实践
        improvement_plan["daily_practices"] = self._design_daily_practices(focus_areas)

        # 设计周度复盘
        improvement_plan["weekly_reviews"] = self._design_weekly_reviews(focus_areas)

        # 设计月度目标
        improvement_plan["monthly_goals"] = self._design_monthly_goals(focus_areas)

        # 推荐学习资源
        for area in focus_areas:
            improvement_plan["learning_resources"][area] = self._recommend_resources(area)

        return improvement_plan

    def optimize_life_rhythm(
        self,
        profile: PersonProfile,
        priorities: List[str]
    ) -> Dict[str, Any]:
        """
        生活节奏优化

        Args:
            priorities: 优先事项列表
        """
        return {
            "energy_management": self._design_energy_plan(profile),
            "time_blocking": self._design_time_blocks(priorities),
            "weekly_structure": self._design_weekly_structure(priorities),
            "recovery_periods": self._design_recovery(profile),
            "peak_performance_windows": self._identify_peak_windows(profile),
            "balance_strategy": self._design_balance_strategy(priorities)
        }

    def design_time_management(
        self,
        profile: PersonProfile,
        goals: List[str]
    ) -> Dict[str, Any]:
        """
        时间管理设计

        Args:
            goals: 目标列表
        """
        return {
            "time_audit": self._conduct_time_audit(profile),
            "priority_matrix": self._create_priority_matrix(goals),
            "scheduling_system": self._design_scheduling_system(goals),
            "focus_techniques": self._recommend_focus_techniques(),
            "distraction_management": self._design_distraction_management(),
            "productivity_tools": self._recommend_productivity_tools(goals)
        }

    def create_reading_plan(
        self,
        topics: List[str],
        duration_months: int = 6,
        reading_speed: str = "medium"
    ) -> Dict[str, Any]:
        """
        读书计划

        Args:
            topics: 主题列表
            duration_months: 持续时间
            reading_speed: 阅读速度（slow/medium/fast）
        """
        books_per_month = {
            "slow": 1,
            "medium": 2,
            "fast": 4
        }.get(reading_speed, 2)

        total_books = books_per_month * duration_months

        return {
            "reading_list": self._curate_reading_list(topics, total_books),
            "reading_schedule": self._design_reading_schedule(total_books, duration_months),
            "note_taking_system": self._design_note_system(),
            "reflection_practice": self._design_reflection_practice(),
            "knowledge_application": self._design_application_plan(topics),
            "discussion_plan": self._design_discussion_plan()
        }

    def _generate_phases(
        self,
        plan_type: str,
        duration_months: int,
        goal: str
    ) -> List[Dict[str, Any]]:
        """生成阶段性计划"""
        phase_templates = {
            "career": [
                {"name": "准备期", "ratio": 0.2, "focus": "技能提升与信息收集"},
                {"name": "行动期", "ratio": 0.4, "focus": "主动求职与面试"},
                {"name": "过渡期", "ratio": 0.2, "focus": "入职适应与角色建立"},
                {"name": "发展期", "ratio": 0.2, "focus": "深度融入与价值创造"}
            ],
            "skill": [
                {"name": "基础期", "ratio": 0.3, "focus": "理论学习与概念理解"},
                {"name": "实践期", "ratio": 0.4, "focus": "项目实战与经验积累"},
                {"name": "精通期", "ratio": 0.3, "focus": "高级应用与创新"}
            ],
            "health": [
                {"name": "适应期", "ratio": 0.25, "focus": "建立运动习惯"},
                {"name": "强化期", "ratio": 0.5, "focus": "持续训练与突破"},
                {"name": "稳定期", "ratio": 0.25, "focus": "保持与优化"}
            ],
            "lifestyle": [
                {"name": "评估期", "ratio": 0.15, "focus": "现状分析与目标设定"},
                {"name": "改变期", "ratio": 0.5, "focus": "新习惯建立"},
                {"name": "优化期", "ratio": 0.35, "focus": "持续优化与调整"}
            ]
        }

        templates = phase_templates.get(plan_type, phase_templates["lifestyle"])
        phases = []

        accumulated_months = 0
        for template in templates:
            phase_duration = int(duration_months * template["ratio"])
            phases.append({
                "phase_name": template["name"],
                "duration_months": phase_duration,
                "start_month": accumulated_months,
                "end_month": accumulated_months + phase_duration,
                "focus_area": template["focus"],
                "key_activities": self._generate_phase_activities(plan_type, template["name"]),
                "expected_outcomes": self._generate_phase_outcomes(plan_type, template["name"])
            })
            accumulated_months += phase_duration

        return phases

    def _generate_milestones(
        self,
        plan_type: str,
        duration_months: int
    ) -> List[str]:
        """生成里程碑"""
        milestone_density = max(4, duration_months // 3)
        milestones = []

        milestone_templates = {
            "career": [
                "完成目标职位调研",
                "简历优化完成",
                "获得第一次面试",
                "收到offer",
                "成功入职",
                "通过试用期",
                "获得第一次晋升机会"
            ],
            "skill": [
                "掌握基础概念",
                "完成第一个项目",
                "获得认证/证书",
                "独立解决复杂问题",
                "能够指导他人",
                "成为该领域专家"
            ],
            "health": [
                "建立稳定运动习惯",
                "体能测试提升20%",
                "达到目标体重/体脂",
                "完成高强度挑战",
                "保持6个月无反弹"
            ]
        }

        templates = milestone_templates.get(plan_type, [
            f"第{i}个月目标达成" for i in range(1, milestone_density + 1)
        ])

        # 根据时长选择合适数量的里程碑
        num_milestones = min(len(templates), milestone_density)
        milestones = templates[:num_milestones]

        return milestones

    def _design_habit_system(
        self,
        plan_type: str,
        profile: PersonProfile
    ) -> Dict[str, Any]:
        """设计习惯系统"""
        return {
            "daily_habits": self._define_daily_habits(plan_type),
            "weekly_habits": self._define_weekly_habits(plan_type),
            "trigger_points": self._identify_triggers(plan_type),
            "reward_mechanisms": self._design_reward_mechanisms(plan_type),
            "tracking_tools": ["习惯追踪表", "进度日历", "数据看板"],
            "accountability_partners": self._suggest_accountability(profile),
            "habit_stacking": self._design_habit_stacking(plan_type)
        }

    def _identify_resources(self, plan_type: str, goal: str) -> List[str]:
        """识别所需资源"""
        resource_map = {
            "career": [
                "行业导师或教练",
                "在线学习平台会员",
                "专业社交网络",
                "简历优化服务",
                "面试准备资料",
                f"目标领域的专业书籍"
            ],
            "skill": [
                "学习课程或培训",
                "实践项目机会",
                "学习社群",
                "技术书籍和文档",
                "练习环境/工具"
            ],
            "health": [
                "健身房会员或器材",
                "营养计划",
                "运动装备",
                "健康追踪设备",
                "教练或课程"
            ],
            "lifestyle": [
                "时间管理工具",
                "习惯追踪应用",
                "支持性社交环境",
                "相关书籍和课程"
            ]
        }

        return resource_map.get(plan_type, ["时间投入", "学习资源", "实践机会"])

    def _define_success_metrics(self, plan_type: str, goal: str) -> List[str]:
        """定义成功指标"""
        metric_map = {
            "career": [
                "获得目标职位offer",
                "薪资提升达到预期",
                "工作满意度>8/10",
                "职业技能提升可量化",
                "建立专业人脉网络"
            ],
            "skill": [
                "完成N个实践项目",
                "获得专业认证",
                "能够独立解决问题",
                "技能评估达到目标等级",
                "获得同行认可"
            ],
            "health": [
                "体重/体脂达标",
                "体能指标提升X%",
                "保持运动习惯180天",
                "健康检查指标正常",
                "精力充沛度提升"
            ],
            "lifestyle": [
                "习惯坚持率>80%",
                "时间利用效率提升",
                "生活满意度提升",
                "压力水平降低",
                "整体幸福感提升"
            ]
        }

        return metric_map.get(plan_type, [
            "目标完成度>80%",
            "持续性>6个月",
            "自我评估满意"
        ])

    def _define_core_habits(self, target_area: str) -> List[Dict[str, Any]]:
        """定义核心习惯"""
        habit_map = {
            "productivity": [
                {"habit": "早晨计划当天任务", "frequency": "每天", "time": "5分钟"},
                {"habit": "番茄工作法专注", "frequency": "每天3-4次", "time": "25分钟/次"},
                {"habit": "晚间复盘总结", "frequency": "每天", "time": "10分钟"}
            ],
            "health": [
                {"habit": "早晨运动", "frequency": "每天", "time": "30分钟"},
                {"habit": "健康饮食", "frequency": "每餐", "time": "准备+用餐"},
                {"habit": "充足睡眠", "frequency": "每晚", "time": "7-8小时"}
            ],
            "learning": [
                {"habit": "主题阅读", "frequency": "每天", "time": "30-60分钟"},
                {"habit": "实践练习", "frequency": "每天", "time": "45分钟"},
                {"habit": "知识整理", "frequency": "每周", "time": "2小时"}
            ]
        }

        return habit_map.get(target_area, [
            {"habit": "专注时间", "frequency": "每天", "time": "1小时"},
            {"habit": "反思总结", "frequency": "每周", "time": "30分钟"}
        ])

    def _design_triggers(self, target_area: str) -> List[str]:
        """设计触发器"""
        return [
            "时间触发：固定时间点执行",
            "事件触发：完成某事后立即执行",
            "环境触发：进入特定场所自动启动",
            "情绪触发：感到某种状态时执行"
        ]

    def _design_rewards(self, target_area: str) -> Dict[str, List[str]]:
        """设计奖励系统"""
        return {
            "即时奖励": ["完成打卡", "进度可视化", "成就感"],
            "短期奖励": ["周度总结奖励", "里程碑庆祝"],
            "长期奖励": ["能力提升", "生活改善", "目标达成"]
        }

    def _design_tracking(self, target_area: str) -> Dict[str, Any]:
        """设计追踪方法"""
        return {
            "工具": ["习惯追踪App", "纸质日历", "电子表格"],
            "指标": ["连续天数", "完成率", "质量评分"],
            "可视化": ["进度条", "热力图", "趋势图"]
        }

    def _design_accountability(self, target_area: str) -> List[str]:
        """设计问责机制"""
        return [
            "找一个习惯伙伴互相监督",
            "公开承诺（社交媒体分享进度）",
            "加入相关主题社群",
            "定期向导师/教练汇报"
        ]

    def _design_progression(self, target_area: str) -> List[Dict[str, str]]:
        """设计进阶计划"""
        return [
            {"stage": "第1-30天", "focus": "建立基础习惯，降低难度确保完成"},
            {"stage": "第31-60天", "focus": "提升强度和质量，加入变化"},
            {"stage": "第61-90天", "focus": "习惯内化，自动执行"},
            {"stage": "第91天+", "focus": "优化升级，拓展到相关领域"}
        ]

    def _assess_current_state(
        self,
        profile: PersonProfile,
        focus_areas: List[str]
    ) -> Dict[str, Any]:
        """评估当前状态"""
        return {
            "strengths": profile.skills[:5],
            "improvement_areas": focus_areas,
            "current_level": {area: random.randint(3, 7) for area in focus_areas},
            "target_level": {area: 9 for area in focus_areas},
            "gap_analysis": {area: f"需要提升{9 - random.randint(3, 7)}个等级" for area in focus_areas}
        }

    def _create_growth_roadmap(self, area: str, profile: PersonProfile) -> Dict[str, Any]:
        """创建成长路线图"""
        return {
            "current_state": f"当前水平：初级-中级",
            "target_state": f"目标水平：高级-专家",
            "learning_path": [
                {"stage": "基础夯实", "duration": "1-2月", "activities": ["理论学习", "概念理解"]},
                {"stage": "实践应用", "duration": "3-6月", "activities": ["项目实战", "经验积累"]},
                {"stage": "深度精通", "duration": "7-12月", "activities": ["高级技巧", "创新应用"]}
            ],
            "key_resources": self._recommend_resources(area),
            "practice_projects": [f"{area}项目{i}" for i in range(1, 4)]
        }

    def _design_daily_practices(self, focus_areas: List[str]) -> List[Dict[str, str]]:
        """设计日常实践"""
        return [
            {"time": "06:30-07:00", "activity": "晨间冥想与目标设定"},
            {"time": "07:00-08:00", "activity": "深度学习时间"},
            {"time": "12:00-12:30", "activity": "午间反思与调整"},
            {"time": "19:00-20:00", "activity": "技能实践时间"},
            {"time": "21:00-21:30", "activity": "每日总结与规划"}
        ]

    def _design_weekly_reviews(self, focus_areas: List[str]) -> List[str]:
        """设计周度复盘"""
        return [
            "本周成就回顾：完成了什么？",
            "学习收获总结：学到了什么？",
            "挑战与障碍：遇到什么困难？如何克服？",
            "习惯执行率：各项习惯完成情况",
            "下周计划调整：需要改进的地方"
        ]

    def _design_monthly_goals(self, focus_areas: List[str]) -> List[Dict[str, Any]]:
        """设计月度目标"""
        return [
            {
                "area": area,
                "goal": f"{area}领域月度突破",
                "metrics": ["完成2个实践项目", "学习10小时", "输出1篇总结"],
                "deadline": "月末"
            }
            for area in focus_areas
        ]

    def _recommend_resources(self, area: str) -> List[str]:
        """推荐学习资源"""
        generic_resources = [
            f"{area}领域经典书籍3-5本",
            f"{area}在线课程（Coursera/Udemy等）",
            f"{area}专业博客和论文",
            f"{area}实践社区和论坛",
            f"{area}领域专家的分享"
        ]
        return generic_resources

    def _design_energy_plan(self, profile: PersonProfile) -> Dict[str, Any]:
        """设计能量管理计划"""
        return {
            "peak_energy_hours": ["9:00-11:00", "15:00-17:00"],
            "low_energy_hours": ["13:00-14:00", "20:00-21:00"],
            "energy_boosters": ["运动", "小憩", "健康零食", "社交互动"],
            "energy_drainers": ["长时间会议", "多任务切换", "负面信息"],
            "optimization_strategies": [
                "高能量时段做重要工作",
                "低能量时段做简单任务",
                "定期休息恢复"
            ]
        }

    def _design_time_blocks(self, priorities: List[str]) -> List[Dict[str, str]]:
        """设计时间块"""
        return [
            {"time": "06:00-09:00", "block": "深度工作块1", "for": priorities[0] if priorities else "优先任务"},
            {"time": "09:00-12:00", "block": "协作互动块", "for": "会议、沟通"},
            {"time": "13:00-14:00", "block": "休息恢复块", "for": "午餐、放松"},
            {"time": "14:00-17:00", "block": "深度工作块2", "for": priorities[1] if len(priorities) > 1 else "次要任务"},
            {"time": "17:00-19:00", "block": "学习成长块", "for": "阅读、技能提升"},
            {"time": "19:00-21:00", "block": "个人生活块", "for": "运动、家庭、兴趣"},
            {"time": "21:00-22:00", "block": "复盘规划块", "for": "总结、规划"}
        ]

    def _design_weekly_structure(self, priorities: List[str]) -> Dict[str, List[str]]:
        """设计周度结构"""
        return {
            "Monday": ["周计划会议", "重点项目启动"],
            "Tuesday": ["深度工作日", "最重要任务"],
            "Wednesday": ["协作日", "团队沟通"],
            "Thursday": ["深度工作日", "项目推进"],
            "Friday": ["总结复盘", "下周规划"],
            "Saturday": ["学习日", "技能提升"],
            "Sunday": ["休息日", "充电恢复"]
        }

    def _design_recovery(self, profile: PersonProfile) -> Dict[str, Any]:
        """设计恢复期"""
        return {
            "daily_recovery": ["午休15-30分钟", "工作间隙休息5分钟/小时"],
            "weekly_recovery": ["周末1-1.5天完全休息", "周中1晚轻松活动"],
            "monthly_recovery": ["月度放松日", "长周末旅行"],
            "recovery_activities": ["冥想", "散步", "音乐", "社交", "爱好"]
        }

    def _identify_peak_windows(self, profile: PersonProfile) -> List[str]:
        """识别巅峰时段"""
        return [
            "早晨6:00-9:00：认知能力最强，适合创造性工作",
            "上午9:00-12:00：专注力高峰，适合复杂任务",
            "下午15:00-17:00：第二能量高峰，适合协作和执行",
            "晚上19:00-21:00：反思时段，适合学习和规划"
        ]

    def _design_balance_strategy(self, priorities: List[str]) -> Dict[str, Any]:
        """设计平衡策略"""
        return {
            "work_life_ratio": "60:40 (工作:生活)",
            "priority_allocation": {p: f"{100//len(priorities)}%" for p in priorities} if priorities else {},
            "flexibility_buffer": "每周预留20%弹性时间应对突发",
            "boundaries": [
                "工作时间边界：周一至周五9:00-18:00",
                "个人时间保护：晚上和周末",
                "深度工作保护：每天至少2小时不被打扰"
            ],
            "integration_points": [
                "工作中融入学习",
                "运动与社交结合",
                "通勤时间利用"
            ]
        }

    def _conduct_time_audit(self, profile: PersonProfile) -> Dict[str, Any]:
        """进行时间审计"""
        return {
            "current_allocation": {
                "工作": "40-50小时/周",
                "睡眠": "49-56小时/周",
                "个人时间": "30-40小时/周",
                "浪费时间": "估计10-15小时/周"
            },
            "inefficiencies": [
                "社交媒体过度使用",
                "会议效率低下",
                "任务切换过于频繁"
            ],
            "opportunities": [
                "通勤时间利用（学习/阅读）",
                "碎片时间整合",
                "流程自动化"
            ]
        }

    def _create_priority_matrix(self, goals: List[str]) -> Dict[str, List[str]]:
        """创建优先级矩阵"""
        return {
            "紧急且重要": [goals[0] if goals else "核心目标"],
            "重要不紧急": [goals[1] if len(goals) > 1 else "长期规划", "技能提升", "健康管理"],
            "紧急不重要": ["部分会议", "某些邮件"],
            "不紧急不重要": ["社交媒体", "无意义娱乐"]
        }

    def _design_scheduling_system(self, goals: List[str]) -> Dict[str, Any]:
        """设计日程系统"""
        return {
            "planning_rhythm": {
                "年度": "设定年度目标和主题",
                "季度": "制定季度OKR",
                "月度": "分解月度计划",
                "周度": "详细周计划",
                "日度": "当日任务清单"
            },
            "scheduling_principles": [
                "重要事项优先安排",
                "深度工作时段保护",
                "缓冲时间预留",
                "定期复盘时间固定"
            ],
            "tools": ["日历工具", "任务管理App", "时间追踪软件"]
        }

    def _recommend_focus_techniques(self) -> List[Dict[str, str]]:
        """推荐专注技巧"""
        return [
            {"technique": "番茄工作法", "description": "25分钟专注+5分钟休息"},
            {"technique": "深度工作", "description": "90-120分钟无干扰专注"},
            {"technique": "时间盒", "description": "为任务设定固定时间框"},
            {"technique": "单任务模式", "description": "同时只做一件事"},
            {"technique": "环境优化", "description": "创造无干扰工作环境"}
        ]

    def _design_distraction_management(self) -> Dict[str, List[str]]:
        """设计干扰管理"""
        return {
            "预防措施": [
                "手机静音或放置远处",
                "关闭通知",
                "使用网站屏蔽工具",
                "告知他人工作时间"
            ],
            "应对策略": [
                "记录干扰事项稍后处理",
                "设置固定查看邮件时间",
                "培养抗干扰能力"
            ]
        }

    def _recommend_productivity_tools(self, goals: List[str]) -> List[str]:
        """推荐生产力工具"""
        return [
            "任务管理：Todoist, Things, TickTick",
            "时间追踪：RescueTime, Toggl",
            "专注辅助：Forest, Focus@Will",
            "笔记系统：Notion, Obsidian, Roam Research",
            "日历工具：Google Calendar, Fantastical",
            "习惯追踪：Habitica, Streaks"
        ]

    def _curate_reading_list(self, topics: List[str], total_books: int) -> List[Dict[str, str]]:
        """策划阅读清单"""
        books_per_topic = total_books // len(topics) if topics else total_books

        reading_list = []
        for topic in topics:
            for i in range(books_per_topic):
                reading_list.append({
                    "topic": topic,
                    "title": f"{topic}领域经典书籍 #{i+1}",
                    "difficulty": ["入门", "进阶", "高级"][i % 3],
                    "estimated_time": f"{random.randint(10, 30)}天"
                })

        return reading_list[:total_books]

    def _design_reading_schedule(
        self,
        total_books: int,
        duration_months: int
    ) -> Dict[str, Any]:
        """设计阅读时间表"""
        return {
            "pace": f"{total_books / duration_months:.1f}本/月",
            "daily_reading": "30-60分钟",
            "weekly_review": "周日下午2小时",
            "reading_blocks": [
                "早晨30分钟",
                "通勤时间",
                "睡前30分钟"
            ]
        }

    def _design_note_system(self) -> Dict[str, Any]:
        """设计笔记系统"""
        return {
            "method": "康奈尔笔记法 + 卡片盒笔记法",
            "structure": {
                "阅读笔记": "关键概念、精彩段落",
                "思考笔记": "个人见解、质疑",
                "行动笔记": "可应用的要点"
            },
            "tools": ["Notion", "Obsidian", "纸质笔记本"],
            "review_cycle": "每周复习一次笔记"
        }

    def _design_reflection_practice(self) -> List[str]:
        """设计反思实践"""
        return [
            "阅读后立即写下3个关键收获",
            "每本书完成后写读书报告",
            "月度主题总结与知识整合",
            "与他人讨论交流深化理解"
        ]

    def _design_application_plan(self, topics: List[str]) -> Dict[str, List[str]]:
        """设计应用计划"""
        return {
            topic: [
                f"识别{topic}在工作中的应用场景",
                f"设计{topic}相关的实践项目",
                f"分享{topic}知识给他人"
            ]
            for topic in topics
        }

    def _design_discussion_plan(self) -> Dict[str, str]:
        """设计讨论计划"""
        return {
            "frequency": "每2周一次",
            "format": "读书会或一对一讨论",
            "structure": "分享-讨论-辩论-总结",
            "output": "讨论笔记和新见解"
        }

    def _generate_phase_activities(self, plan_type: str, phase_name: str) -> List[str]:
        """生成阶段活动"""
        activities_map = {
            "准备期": ["信息收集", "技能评估", "资源准备", "计划制定"],
            "行动期": ["主动执行", "持续实践", "反馈调整"],
            "过渡期": ["适应变化", "巩固成果", "建立新常态"],
            "发展期": ["深化发展", "拓展边界", "创造价值"]
        }

        return activities_map.get(phase_name, ["执行计划", "监测进度", "及时调整"])

    def _generate_phase_outcomes(self, plan_type: str, phase_name: str) -> List[str]:
        """生成阶段预期成果"""
        outcomes_map = {
            "准备期": ["目标清晰", "计划完整", "资源就位"],
            "行动期": ["初步成果", "经验积累", "信心建立"],
            "过渡期": ["稳定状态", "新习惯形成"],
            "发展期": ["目标达成", "持续改善", "新机会涌现"]
        }

        return outcomes_map.get(phase_name, ["按计划推进", "达到阶段目标"])

    def _define_daily_habits(self, plan_type: str) -> List[str]:
        """定义每日习惯"""
        return [
            "早晨目标回顾（5分钟）",
            "专注时间投入（1-2小时）",
            "进度记录（5分钟）",
            "晚间复盘（10分钟）"
        ]

    def _define_weekly_habits(self, plan_type: str) -> List[str]:
        """定义每周习惯"""
        return [
            "周计划制定",
            "周度复盘与调整",
            "学习新知识",
            "社交或人脉拓展"
        ]

    def _identify_triggers(self, plan_type: str) -> List[str]:
        """识别触发点"""
        return [
            "早晨起床后",
            "到达工作地点",
            "午餐后",
            "晚餐前",
            "睡前"
        ]

    def _design_reward_mechanisms(self, plan_type: str) -> List[str]:
        """设计奖励机制"""
        return [
            "每日完成后打卡",
            "每周达标奖励自己",
            "每月里程碑庆祝",
            "最终目标达成大奖"
        ]

    def _suggest_accountability(self, profile: PersonProfile) -> List[str]:
        """建议问责伙伴"""
        return [
            "寻找志同道合的伙伴",
            "加入相关主题社群",
            "雇佣教练或导师",
            "公开承诺并定期分享进度"
        ]

    def _design_habit_stacking(self, plan_type: str) -> List[str]:
        """设计习惯堆叠"""
        return [
            "早晨：冥想 → 计划 → 深度工作",
            "工作后：运动 → 晚餐 → 阅读",
            "睡前：复盘 → 规划 → 放松"
        ]
