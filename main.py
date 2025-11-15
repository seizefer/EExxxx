#!/usr/bin/env python3
"""
人生实验仿真引擎 - 主程序
Life Simulation Engine - Main CLI

这个系统帮助你：
1. 模拟多条人生路径，预见未来可能性
2. 制定生活规划，优化人生轨迹
3. 建立知识体系，深度学习任何主题
4. 生成每日报告，追踪成长进度
"""

import sys
import json
from typing import Dict, Any
from models import PersonProfile
from life_simulator import LifeSimulator
from life_planner import LifePlanner
from knowledge_builder import KnowledgeBuilder
from daily_reporter import DailyReporter
from utils import save_to_json, format_date


class LifeSimulationCLI:
    """人生仿真引擎 CLI"""

    def __init__(self):
        self.simulator = LifeSimulator()
        self.planner = LifePlanner()
        self.knowledge_builder = KnowledgeBuilder()
        self.reporter = DailyReporter()
        self.current_profile = None

    def show_banner(self):
        """显示欢迎横幅"""
        banner = """
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║           🌟 人生实验仿真引擎 v1.0 🌟                       ║
║          Life Simulation Engine                            ║
║                                                            ║
║     探索无限可能 · 规划美好未来 · 持续成长进化               ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
        """
        print(banner)

    def show_menu(self):
        """显示主菜单"""
        menu = """
【主菜单】

1️⃣  多路径人生模拟
   - 模拟5种不同的人生路线
   - 深度推演未来5年
   - 对比分析各路径优劣

2️⃣  生活规划师
   - 未来规划设计
   - 习惯系统建立
   - 自我提升方案
   - 时间管理优化
   - 读书计划制定

3️⃣  知识体系建立
   - 20层知识图谱构建
   - 跨文献推理分析
   - 抽象框架提炼
   - 生成知识电子书

4️⃣  生活自动报告
   - 每日大脑总结
   - 成长洞察分析
   - 明日建议生成
   - 周度趋势报告

5️⃣  个人档案管理
   - 创建/更新个人档案
   - 查看当前档案

0️⃣  退出系统

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
        """
        print(menu)

    def create_profile(self) -> PersonProfile:
        """创建个人档案"""
        print("\n【创建个人档案】\n")

        name = input("你的名字: ").strip() or "探索者"
        age_input = input("你的年龄: ").strip()
        age = int(age_input) if age_input.isdigit() else 28

        current_career = input("当前职业: ").strip() or "职场人"
        education = input("教育背景: ").strip() or "本科"

        print("\n技能列表（用逗号分隔）: ")
        skills_input = input().strip()
        skills = [s.strip() for s in skills_input.split(",")] if skills_input else ["学习能力", "执行力"]

        print("\n兴趣爱好（用逗号分隔）: ")
        interests_input = input().strip()
        interests = [i.strip() for i in interests_input.split(",")] if interests_input else ["科技", "阅读"]

        print("\n目标（用逗号分隔）: ")
        goals_input = input().strip()
        goals = [g.strip() for g in goals_input.split(",")] if goals_input else ["职业发展", "持续学习"]

        profile = PersonProfile(
            name=name,
            age=age,
            current_career=current_career,
            education=education,
            skills=skills,
            interests=interests,
            financial_status="medium",
            health_status="good",
            relationship_status="stable",
            personality_traits=["积极主动", "善于思考"],
            goals=goals,
            constraints=[]
        )

        self.current_profile = profile
        print(f"\n✅ 个人档案创建成功！欢迎，{name}！\n")

        return profile

    def run_life_simulation(self):
        """运行人生模拟"""
        if not self.current_profile:
            print("\n⚠️  请先创建个人档案！\n")
            self.current_profile = self.create_profile()

        print("\n【多路径人生模拟】\n")
        print("正在为你生成5条不同的人生路径...\n")

        years_input = input("模拟年限（默认5年）: ").strip()
        years = int(years_input) if years_input.isdigit() else 5

        # 运行模拟
        result = self.simulator.create_simulation(
            profile=self.current_profile,
            num_paths=5,
            years=years
        )

        # 显示结果
        print(f"\n{'='*60}")
        print(f"【模拟完成】 ID: {result.simulation_id}")
        print(f"{'='*60}\n")

        # 显示各条路径
        for i, path in enumerate(result.paths, 1):
            print(f"\n{i}. {path.title}")
            print(f"   类型: {path.path_type.value}")
            print(f"   成功概率: {path.success_probability:.1%}")
            print(f"   风险等级: {path.risk_level}")
            print(f"   描述: {path.description}")
            print(f"\n   关键因素:")
            for factor in path.key_factors[:3]:
                print(f"   • {factor}")

            print(f"\n   5年后预测:")
            final = path.final_state
            print(f"   • 职业: {final.get('career_position', '未知')}")
            print(f"   • 财务: {final.get('financial_status', '未知')}")
            print(f"   • 生活满意度: {final.get('life_satisfaction', 0)}/10")

            print(f"\n   主要成就:")
            for achievement in final.get('achievements', [])[:3]:
                print(f"   ✓ {achievement}")

            print(f"\n{'-'*60}")

        # 显示洞察
        print(f"\n【深度洞察】\n")
        for i, insight in enumerate(result.insights, 1):
            print(f"{i}. {insight}\n")

        # 显示建议
        print(f"\n【行动建议】\n")
        for i, rec in enumerate(result.recommendations, 1):
            print(f"{i}. {rec}\n")

        # 保存结果
        filename = f"simulation_{result.simulation_id}.json"
        save_to_json(self._serialize_simulation(result), filename)
        print(f"\n💾 完整结果已保存到: {filename}\n")

    def run_life_planning(self):
        """运行生活规划"""
        print("\n【生活规划师】\n")
        print("1. 未来规划")
        print("2. 习惯系统")
        print("3. 自我提升方案")
        print("4. 生活节奏优化")
        print("5. 时间管理设计")
        print("6. 读书计划")
        print("\n选择功能: ")

        choice = input().strip()

        if choice == "1":
            self._create_future_plan()
        elif choice == "2":
            self._create_habit_system()
        elif choice == "3":
            self._create_improvement_plan()
        elif choice == "4":
            self._optimize_life_rhythm()
        elif choice == "5":
            self._design_time_management()
        elif choice == "6":
            self._create_reading_plan()
        else:
            print("\n⚠️  无效选择\n")

    def _create_future_plan(self):
        """创建未来规划"""
        if not self.current_profile:
            self.current_profile = self.create_profile()

        print("\n【未来规划设计】\n")
        print("规划类型:")
        print("1. 职业发展 (career)")
        print("2. 技能学习 (skill)")
        print("3. 健康管理 (health)")
        print("4. 生活方式 (lifestyle)")

        plan_type_map = {"1": "career", "2": "skill", "3": "health", "4": "lifestyle"}
        type_choice = input("\n选择类型: ").strip()
        plan_type = plan_type_map.get(type_choice, "lifestyle")

        goal = input("具体目标: ").strip() or "实现自我提升"

        months_input = input("规划时长（月，默认12）: ").strip()
        months = int(months_input) if months_input.isdigit() else 12

        print("\n正在生成规划...\n")

        plan = self.planner.create_future_plan(
            profile=self.current_profile,
            plan_type=plan_type,
            goal=goal,
            duration_months=months
        )

        print(f"{'='*60}")
        print(f"【{plan.title}】")
        print(f"{'='*60}\n")

        print(f"时长: {plan.duration_months}个月\n")

        print("【阶段规划】\n")
        for phase in plan.phases:
            print(f"📍 {phase['phase_name']} ({phase['duration_months']}个月)")
            print(f"   重点: {phase['focus_area']}")
            print(f"   关键活动: {', '.join(phase['key_activities'][:3])}")
            print(f"   预期成果: {', '.join(phase['expected_outcomes'][:2])}\n")

        print("【里程碑】\n")
        for milestone in plan.milestones:
            print(f"✓ {milestone}")

        print("\n【所需资源】\n")
        for resource in plan.resources_needed[:5]:
            print(f"• {resource}")

        print("\n【成功指标】\n")
        for metric in plan.success_metrics[:5]:
            print(f"→ {metric}")

        filename = f"plan_{format_date()}.json"
        save_to_json(self._serialize_plan(plan), filename)
        print(f"\n💾 规划已保存到: {filename}\n")

    def _create_habit_system(self):
        """创建习惯系统"""
        if not self.current_profile:
            self.current_profile = self.create_profile()

        print("\n【习惯系统建立】\n")
        print("目标领域:")
        print("1. 生产力 (productivity)")
        print("2. 健康 (health)")
        print("3. 学习 (learning)")

        area_map = {"1": "productivity", "2": "health", "3": "learning"}
        area_choice = input("\n选择领域: ").strip()
        target_area = area_map.get(area_choice, "productivity")

        print("\n正在设计习惯系统...\n")

        habit_system = self.planner.create_habit_system(
            profile=self.current_profile,
            target_area=target_area
        )

        print(f"{'='*60}")
        print(f"【{habit_system['target_area']}习惯系统】")
        print(f"{'='*60}\n")

        print("【核心习惯】\n")
        for habit in habit_system['core_habits']:
            print(f"• {habit['habit']}")
            print(f"  频率: {habit['frequency']}")
            print(f"  时长: {habit['time']}\n")

        print("【触发设计】\n")
        for trigger in habit_system['trigger_design'][:3]:
            print(f"→ {trigger}")

        print("\n【奖励机制】\n")
        for category, rewards in habit_system['reward_system'].items():
            print(f"{category}: {', '.join(rewards)}")

        print("\n【进阶路径】\n")
        for stage in habit_system['progression_plan']:
            print(f"{stage['stage']}: {stage['focus']}\n")

        filename = f"habits_{target_area}_{format_date()}.json"
        save_to_json(habit_system, filename)
        print(f"💾 习惯系统已保存到: {filename}\n")

    def _create_improvement_plan(self):
        """创建自我提升方案"""
        if not self.current_profile:
            self.current_profile = self.create_profile()

        print("\n【自我提升方案】\n")
        print("关注领域（用逗号分隔）: ")
        areas_input = input().strip()
        focus_areas = [a.strip() for a in areas_input.split(",")] if areas_input else ["技能提升", "思维成长"]

        print("\n正在生成提升方案...\n")

        plan = self.planner.create_self_improvement_plan(
            profile=self.current_profile,
            focus_areas=focus_areas
        )

        print(f"{'='*60}")
        print(f"【自我提升全方位方案】")
        print(f"{'='*60}\n")

        print("【当前状态评估】\n")
        assessment = plan['assessment']
        print(f"优势: {', '.join(assessment['strengths'][:3])}")
        print(f"待提升领域: {', '.join(assessment['improvement_areas'])}\n")

        print("【成长路线图】\n")
        for area, roadmap in list(plan['growth_roadmap'].items())[:2]:
            print(f"📈 {area}")
            print(f"   当前: {roadmap['current_state']}")
            print(f"   目标: {roadmap['target_state']}\n")

        print("【日常实践】\n")
        for practice in plan['daily_practices'][:5]:
            print(f"⏰ {practice['time']}: {practice['activity']}")

        print("\n【月度目标】\n")
        for goal in plan['monthly_goals'][:3]:
            print(f"🎯 {goal['area']}: {goal['goal']}")
            print(f"   指标: {', '.join(goal['metrics'])}\n")

        filename = f"improvement_plan_{format_date()}.json"
        save_to_json(plan, filename)
        print(f"💾 提升方案已保存到: {filename}\n")

    def _optimize_life_rhythm(self):
        """优化生活节奏"""
        print("\n【生活节奏优化】\n")
        print("优先事项（用逗号分隔）: ")
        priorities_input = input().strip()
        priorities = [p.strip() for p in priorities_input.split(",")] if priorities_input else ["工作", "学习", "健康"]

        if not self.current_profile:
            self.current_profile = self.create_profile()

        optimization = self.planner.optimize_life_rhythm(
            profile=self.current_profile,
            priorities=priorities
        )

        print(f"\n{'='*60}")
        print(f"【生活节奏优化方案】")
        print(f"{'='*60}\n")

        print("【能量管理】\n")
        energy = optimization['energy_management']
        print(f"高能量时段: {', '.join(energy['peak_energy_hours'])}")
        print(f"低能量时段: {', '.join(energy['low_energy_hours'])}\n")

        print("【时间块设计】\n")
        for block in optimization['time_blocking'][:5]:
            print(f"{block['time']}: {block['block']} - {block['for']}")

        print("\n【平衡策略】\n")
        balance = optimization['balance_strategy']
        print(f"工作生活比例: {balance['work_life_ratio']}")
        print(f"弹性缓冲: {balance['flexibility_buffer']}\n")

        filename = f"life_rhythm_{format_date()}.json"
        save_to_json(optimization, filename)
        print(f"💾 优化方案已保存到: {filename}\n")

    def _design_time_management(self):
        """设计时间管理"""
        print("\n【时间管理设计】\n")
        print("主要目标（用逗号分隔）: ")
        goals_input = input().strip()
        goals = [g.strip() for g in goals_input.split(",")] if goals_input else ["提高效率", "深度工作"]

        if not self.current_profile:
            self.current_profile = self.create_profile()

        tm_design = self.planner.design_time_management(
            profile=self.current_profile,
            goals=goals
        )

        print(f"\n{'='*60}")
        print(f"【时间管理系统】")
        print(f"{'='*60}\n")

        print("【优先级矩阵】\n")
        for category, items in tm_design['priority_matrix'].items():
            print(f"{category}:")
            for item in items:
                print(f"  • {item}")
            print()

        print("【专注技巧】\n")
        for technique in tm_design['focus_techniques'][:5]:
            print(f"→ {technique['technique']}: {technique['description']}")

        print("\n【推荐工具】\n")
        for tool in tm_design['productivity_tools'][:5]:
            print(f"• {tool}")

        filename = f"time_management_{format_date()}.json"
        save_to_json(tm_design, filename)
        print(f"\n💾 时间管理系统已保存到: {filename}\n")

    def _create_reading_plan(self):
        """创建读书计划"""
        print("\n【读书计划制定】\n")
        print("感兴趣的主题（用逗号分隔）: ")
        topics_input = input().strip()
        topics = [t.strip() for t in topics_input.split(",")] if topics_input else ["个人成长", "技术"]

        months_input = input("计划时长（月，默认6）: ").strip()
        months = int(months_input) if months_input.isdigit() else 6

        print("阅读速度 (slow/medium/fast，默认medium): ")
        speed = input().strip() or "medium"

        reading_plan = self.planner.create_reading_plan(
            topics=topics,
            duration_months=months,
            reading_speed=speed
        )

        print(f"\n{'='*60}")
        print(f"【{months}个月读书计划】")
        print(f"{'='*60}\n")

        print(f"阅读节奏: {reading_plan['reading_schedule']['pace']}\n")

        print("【书单（前10本）】\n")
        for i, book in enumerate(reading_plan['reading_list'][:10], 1):
            print(f"{i}. {book['title']}")
            print(f"   主题: {book['topic']}")
            print(f"   难度: {book['difficulty']}")
            print(f"   预计: {book['estimated_time']}\n")

        print("【笔记系统】\n")
        note_system = reading_plan['note_taking_system']
        print(f"方法: {note_system['method']}")
        print(f"工具: {', '.join(note_system['tools'])}\n")

        filename = f"reading_plan_{format_date()}.json"
        save_to_json(reading_plan, filename)
        print(f"💾 读书计划已保存到: {filename}\n")

    def run_knowledge_building(self):
        """运行知识体系建立"""
        print("\n【知识体系建立】\n")
        print("1. 构建知识图谱")
        print("2. 跨文献推理")
        print("3. 生成知识电子书")
        print("\n选择功能: ")

        choice = input().strip()

        if choice == "1":
            self._build_knowledge_graph()
        elif choice == "2":
            self._perform_cross_reasoning()
        elif choice == "3":
            self._generate_knowledge_book()
        else:
            print("\n⚠️  无效选择\n")

    def _build_knowledge_graph(self):
        """构建知识图谱"""
        print("\n【构建知识图谱】\n")
        print("主题: ")
        topic = input().strip() or "人工智能"

        depth_input = input("深度/层数（默认20）: ").strip()
        depth = int(depth_input) if depth_input.isdigit() else 20

        print("广度 (narrow/medium/wide，默认medium): ")
        breadth = input().strip() or "medium"

        print(f"\n正在构建{depth}层知识图谱...\n")
        print("这可能需要一些时间，请稍候...\n")

        graph = self.knowledge_builder.build_knowledge_graph(
            topic=topic,
            depth=depth,
            breadth=breadth
        )

        print(f"{'='*60}")
        print(f"【{graph.topic} - 知识图谱】")
        print(f"{'='*60}\n")

        print(f"总节点数: {len(graph.nodes)}")
        print(f"最大深度: {graph.max_depth}层")
        print(f"总概念数: {graph.total_concepts}\n")

        # 显示框架
        framework = graph.framework
        print("【知识维度】\n")
        for dim in framework.get('知识维度', [])[:5]:
            print(f"• {dim}")

        print("\n【核心支柱】\n")
        for pillar in framework.get('核心支柱', [])[:5]:
            print(f"→ {pillar.get('标题', '')} (重要性: {pillar.get('重要性', '')})")

        print("\n【知识层次分析】\n")
        hierarchy = framework.get('知识层次', {})
        print(f"总层数: {hierarchy.get('总层数', 0)}")
        print(f"总节点数: {hierarchy.get('总节点数', 0)}")
        print(f"平均每层: {hierarchy.get('平均每层节点数', 0):.1f}个节点\n")

        print("【对称性分析】\n")
        symmetry = framework.get('对称性分析', {})
        print(f"分支数量: {symmetry.get('分支数量', 0)}")
        print(f"平衡度: {symmetry.get('平衡度', '未知')}")
        print(f"对称性评分: {symmetry.get('对称性评分', 0):.2f}\n")

        filename = f"knowledge_graph_{topic}_{format_date()}.json"
        save_to_json(self._serialize_knowledge_graph(graph), filename)
        print(f"💾 知识图谱已保存到: {filename}\n")

    def _perform_cross_reasoning(self):
        """执行跨文献推理"""
        print("\n【跨文献推理分析】\n")
        print("首先，请输入主题: ")
        topic = input().strip() or "人工智能"

        print("\n构建基础知识图谱...\n")
        graph = self.knowledge_builder.build_knowledge_graph(topic, depth=10, breadth="medium")

        print("分析视角（用逗号分隔）: ")
        perspectives_input = input().strip()
        perspectives = [p.strip() for p in perspectives_input.split(",")] if perspectives_input else [
            "技术视角", "哲学视角", "社会视角"
        ]

        print(f"\n正在进行跨文献推理...\n")

        reasoning = self.knowledge_builder.perform_cross_literature_reasoning(
            graph=graph,
            perspectives=perspectives
        )

        print(f"{'='*60}")
        print(f"【{reasoning['主题']} - 跨文献推理】")
        print(f"{'='*60}\n")

        print(f"分析视角: {', '.join(reasoning['分析视角'])}\n")

        print("【交叉发现】\n")
        for finding in reasoning['交叉发现']:
            print(f"从【{finding['视角']}】:")
            print(f"  {finding['核心发现']}\n")

        print("【综合洞察】\n")
        for i, insight in enumerate(reasoning['综合洞察'], 1):
            print(f"{i}. {insight}\n")

        filename = f"cross_reasoning_{topic}_{format_date()}.json"
        save_to_json(reasoning, filename)
        print(f"💾 推理结果已保存到: {filename}\n")

    def _generate_knowledge_book(self):
        """生成知识电子书"""
        print("\n【生成知识电子书】\n")
        print("主题: ")
        topic = input().strip() or "人工智能史"

        print("\n构建知识图谱并生成电子书...\n")
        print("这需要较长时间，请耐心等待...\n")

        graph = self.knowledge_builder.build_knowledge_graph(topic, depth=15, breadth="medium")

        book = self.knowledge_builder.generate_knowledge_book(graph)

        print(f"{'='*60}")
        print(f"【{book['书名']}】")
        print(f"{'='*60}\n")

        print(f"总页数估计: {book['总页数估计']}页\n")

        print("【目录】\n")
        for chapter in book['目录'][:8]:
            print(f"{chapter['章节']}: {chapter['标题']}")
            if chapter.get('小节'):
                for subsection in chapter['小节'][:3]:
                    print(f"  - {subsection}")
            print()

        print("【附录】\n")
        appendix = book['附录']
        print(f"核心概念索引: {len(appendix['核心概念索引'])}个概念")
        print(f"延伸阅读: {len(appendix['延伸阅读'])}本推荐书籍\n")

        print("推荐书籍:")
        for i, book_rec in enumerate(appendix['延伸阅读'][:5], 1):
            print(f"  {i}. {book_rec}")

        filename = f"knowledge_book_{topic}_{format_date()}.json"
        save_to_json(book, filename)
        print(f"\n💾 知识电子书已保存到: {filename}\n")

    def run_daily_reporting(self):
        """运行每日报告"""
        print("\n【生活自动报告系统】\n")
        print("1. 生成今日报告")
        print("2. 查看周度总结")
        print("\n选择功能: ")

        choice = input().strip()

        if choice == "1":
            self._generate_today_report()
        elif choice == "2":
            self._show_weekly_summary()
        else:
            print("\n⚠️  无效选择\n")

    def _generate_today_report(self):
        """生成今日报告"""
        print("\n【今日生活报告】\n")
        print("快速模式（使用示例数据）还是详细模式？(quick/detailed): ")
        mode = input().strip() or "quick"

        if mode == "detailed":
            # 详细输入
            print("\n早晨心情: ")
            morning_mood = input().strip()
            print("下午心情: ")
            afternoon_mood = input().strip()
            print("晚上心情: ")
            evening_mood = input().strip()

            mood_data = {
                "morning": morning_mood or "平静",
                "afternoon": afternoon_mood or "专注",
                "evening": evening_mood or "放松"
            }

            print("\n今天阅读的文章（数量）: ")
            articles_count = int(input().strip() or "2")
            print("今天观看的视频（数量）: ")
            videos_count = int(input().strip() or "1")

            input_data = {
                "articles": [f"文章{i+1}" for i in range(articles_count)],
                "videos": [f"视频{i+1}" for i in range(videos_count)]
            }

            activities = []
        else:
            # 快速模式
            mood_data = None
            input_data = None
            activities = None

        print("\n正在分析今日数据...\n")

        report = self.reporter.generate_daily_report(
            mood_data=mood_data,
            input_data=input_data,
            activities=activities
        )

        print(f"{'='*60}")
        print(f"【{report.date} 每日报告】")
        print(f"{'='*60}\n")

        print(report.brain_summary)
        print()

        print("【成长洞察】\n")
        for i, insight in enumerate(report.growth_insights, 1):
            print(f"{i}. {insight}\n")

        print("【明日建议】\n")
        for suggestion in report.tomorrow_suggestions:
            print(f"{suggestion}")

        print(f"\n{'='*60}")
        print("【今日指标】")
        print(f"{'='*60}\n")

        for metric, score in report.metrics.items():
            bar = "█" * int(score) + "░" * (10 - int(score))
            print(f"{metric}: {bar} {score}/10")

        print()

        filename = f"daily_report_{report.date}.json"
        save_to_json(self._serialize_daily_report(report), filename)
        print(f"💾 报告已保存到: {filename}\n")

    def _show_weekly_summary(self):
        """显示周度总结"""
        if len(self.reporter.report_history) < 7:
            print(f"\n⚠️  需要至少7天的数据，当前只有{len(self.reporter.report_history)}天\n")
            print("请先生成一些每日报告！\n")
            return

        summary = self.reporter.generate_weekly_summary(days=7)

        print(f"\n{'='*60}")
        print(f"【{summary['周期']}总结】")
        print(f"{'='*60}\n")

        print("【情绪趋势】\n")
        mood_trend = summary['情绪趋势']
        print(f"积极天数: {mood_trend['积极天数']}")
        print(f"积极率: {mood_trend['积极率']}")
        print(f"趋势: {mood_trend['趋势']}\n")

        print("【成长轨迹】\n")
        growth = summary['成长轨迹']
        print(f"平均成长分数: {growth['平均成长分数']}")
        print(f"波动性: {growth['波动性']}\n")

        print("【主题分布】\n")
        for theme in summary['主题分布']:
            print(f"• {theme}")

        print("\n【平均指标】\n")
        for metric, value in summary['平均指标'].items():
            bar = "█" * int(value) + "░" * (10 - int(value))
            print(f"{metric}: {bar} {value}/10")

        print("\n【亮点时刻】\n")
        for highlight in summary['亮点时刻']:
            print(f"⭐ {highlight}")

        print("\n【改进建议】\n")
        for i, rec in enumerate(summary['改进建议'], 1):
            print(f"{i}. {rec}\n")

        filename = f"weekly_summary_{format_date()}.json"
        save_to_json(summary, filename)
        print(f"💾 周度总结已保存到: {filename}\n")

    def manage_profile(self):
        """管理个人档案"""
        print("\n【个人档案管理】\n")
        print("1. 创建新档案")
        print("2. 查看当前档案")
        print("\n选择操作: ")

        choice = input().strip()

        if choice == "1":
            self.create_profile()
        elif choice == "2":
            if self.current_profile:
                self._show_profile()
            else:
                print("\n⚠️  还没有创建档案，请先创建！\n")
                self.create_profile()
        else:
            print("\n⚠️  无效选择\n")

    def _show_profile(self):
        """显示个人档案"""
        p = self.current_profile

        print(f"\n{'='*60}")
        print(f"【{p.name}的个人档案】")
        print(f"{'='*60}\n")

        print(f"年龄: {p.age}岁")
        print(f"职业: {p.current_career}")
        print(f"教育: {p.education}\n")

        print(f"技能: {', '.join(p.skills)}")
        print(f"兴趣: {', '.join(p.interests)}\n")

        print(f"目标:")
        for goal in p.goals:
            print(f"  • {goal}")

        print(f"\n财务状况: {p.financial_status}")
        print(f"健康状况: {p.health_status}")
        print(f"关系状态: {p.relationship_status}\n")

    def _serialize_simulation(self, result) -> dict:
        """序列化模拟结果"""
        return {
            "simulation_id": result.simulation_id,
            "created_at": result.created_at,
            "paths": [
                {
                    "path_id": p.path_id,
                    "title": p.title,
                    "type": p.path_type.value,
                    "description": p.description,
                    "success_probability": p.success_probability,
                    "risk_level": p.risk_level,
                    "final_state": p.final_state
                }
                for p in result.paths
            ],
            "insights": result.insights,
            "recommendations": result.recommendations
        }

    def _serialize_plan(self, plan) -> dict:
        """序列化规划"""
        return {
            "plan_type": plan.plan_type,
            "title": plan.title,
            "duration_months": plan.duration_months,
            "phases": plan.phases,
            "milestones": plan.milestones,
            "resources_needed": plan.resources_needed,
            "success_metrics": plan.success_metrics
        }

    def _serialize_knowledge_graph(self, graph) -> dict:
        """序列化知识图谱"""
        return {
            "topic": graph.topic,
            "max_depth": graph.max_depth,
            "total_nodes": len(graph.nodes),
            "total_concepts": graph.total_concepts,
            "framework": graph.framework,
            "nodes": [
                {
                    "node_id": n.node_id,
                    "title": n.title,
                    "level": n.level,
                    "concepts": n.concepts,
                    "importance": n.importance_score
                }
                for n in graph.nodes[:100]  # 只保存前100个节点
            ]
        }

    def _serialize_daily_report(self, report) -> dict:
        """序列化每日报告"""
        return {
            "date": report.date,
            "mood_analysis": report.mood_analysis,
            "brain_summary": report.brain_summary,
            "growth_insights": report.growth_insights,
            "tomorrow_suggestions": report.tomorrow_suggestions,
            "metrics": report.metrics
        }

    def run(self):
        """运行主程序"""
        self.show_banner()

        while True:
            self.show_menu()
            choice = input("请选择功能 (0-5): ").strip()

            if choice == "0":
                print("\n👋 感谢使用人生实验仿真引擎！祝你探索愉快！\n")
                sys.exit(0)
            elif choice == "1":
                self.run_life_simulation()
            elif choice == "2":
                self.run_life_planning()
            elif choice == "3":
                self.run_knowledge_building()
            elif choice == "4":
                self.run_daily_reporting()
            elif choice == "5":
                self.manage_profile()
            else:
                print("\n⚠️  无效选择，请重新输入\n")

            input("\n按 Enter 继续...")


def main():
    """主函数"""
    cli = LifeSimulationCLI()
    try:
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 程序已退出！\n")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ 错误: {e}\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
