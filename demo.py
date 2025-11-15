#!/usr/bin/env python3
"""
人生实验仿真引擎 - 快速演示
Life Simulation Engine - Quick Demo

这个脚本展示如何通过代码直接使用各个模块
"""

from models import PersonProfile
from life_simulator import LifeSimulator
from life_planner import LifePlanner
from knowledge_builder import KnowledgeBuilder
from daily_reporter import DailyReporter


def demo_life_simulation():
    """演示：人生路径模拟"""
    print("\n" + "="*60)
    print("演示1: 多路径人生模拟")
    print("="*60 + "\n")

    # 创建个人档案
    profile = PersonProfile(
        name="探索者",
        age=28,
        current_career="软件工程师",
        education="本科",
        skills=["Python", "机器学习", "产品思维"],
        interests=["人工智能", "个人成长", "创业"],
        financial_status="medium",
        health_status="good",
        relationship_status="stable",
        personality_traits=["积极主动", "善于学习", "执行力强"],
        goals=["转型AI领域", "持续学习", "个人成长"],
        constraints=[]
    )

    # 运行模拟
    print("正在模拟5条不同的人生路径...\n")
    simulator = LifeSimulator()
    result = simulator.create_simulation(profile, num_paths=5, years=5)

    # 显示结果摘要
    print(f"模拟ID: {result.simulation_id}\n")

    for i, path in enumerate(result.paths, 1):
        print(f"\n路径 {i}: {path.title}")
        print(f"  类型: {path.path_type.value}")
        print(f"  成功概率: {path.success_probability:.1%}")
        print(f"  风险等级: {path.risk_level}")
        print(f"  5年后职业: {path.final_state.get('career_position', '未知')}")
        print(f"  生活满意度: {path.final_state.get('life_satisfaction', 0)}/10")

    print("\n【核心洞察】")
    for insight in result.insights[:2]:
        print(f"• {insight}")

    print("\n【建议】")
    for rec in result.recommendations[:2]:
        print(f"→ {rec}")


def demo_life_planning():
    """演示：生活规划"""
    print("\n" + "="*60)
    print("演示2: 生活规划 - 未来12个月技能学习计划")
    print("="*60 + "\n")

    profile = PersonProfile(
        name="学习者",
        age=25,
        current_career="产品经理",
        education="本科",
        skills=["产品设计", "用户研究"],
        interests=["AI", "编程"],
        goals=["学习AI和编程"],
        constraints=[]
    )

    planner = LifePlanner()

    # 创建学习规划
    print("正在生成12个月的技能学习规划...\n")
    plan = planner.create_future_plan(
        profile=profile,
        plan_type="skill",
        goal="深度学习AI和Python编程",
        duration_months=12
    )

    print(f"规划: {plan.title}\n")

    print("【阶段规划】")
    for phase in plan.phases:
        print(f"\n{phase['phase_name']} ({phase['duration_months']}个月)")
        print(f"  重点: {phase['focus_area']}")
        print(f"  活动: {', '.join(phase['key_activities'][:2])}")

    print("\n【里程碑】")
    for milestone in plan.milestones[:5]:
        print(f"✓ {milestone}")

    print("\n【成功指标】")
    for metric in plan.success_metrics[:3]:
        print(f"→ {metric}")


def demo_habit_system():
    """演示：习惯系统"""
    print("\n" + "="*60)
    print("演示3: 习惯系统 - 学习习惯建立")
    print("="*60 + "\n")

    profile = PersonProfile(
        name="习惯养成者",
        age=30,
        current_career="自由职业",
        education="硕士",
        skills=["自律", "时间管理"],
        interests=["学习", "成长"],
        goals=["建立学习习惯"],
        constraints=[]
    )

    planner = LifePlanner()

    print("正在设计学习习惯系统...\n")
    habit_system = planner.create_habit_system(
        profile=profile,
        target_area="learning"
    )

    print(f"目标领域: {habit_system['target_area']}\n")

    print("【核心习惯】")
    for habit in habit_system['core_habits']:
        print(f"• {habit['habit']}")
        print(f"  频率: {habit['frequency']}, 时长: {habit['time']}")

    print("\n【奖励机制】")
    for category, rewards in habit_system['reward_system'].items():
        print(f"{category}: {', '.join(rewards[:2])}")

    print("\n【进阶路径】")
    for stage in habit_system['progression_plan'][:3]:
        print(f"{stage['stage']}: {stage['focus']}")


def demo_knowledge_graph():
    """演示：知识图谱构建"""
    print("\n" + "="*60)
    print("演示4: 知识图谱 - 人工智能史")
    print("="*60 + "\n")

    print("正在构建知识图谱（这可能需要几秒钟）...\n")

    builder = KnowledgeBuilder()
    graph = builder.build_knowledge_graph(
        topic="人工智能史",
        depth=15,
        breadth="medium"
    )

    print(f"主题: {graph.topic}")
    print(f"总节点数: {len(graph.nodes)}")
    print(f"最大深度: {graph.max_depth}层")
    print(f"总概念数: {graph.total_concepts}\n")

    framework = graph.framework

    print("【知识维度】")
    for dim in framework.get('知识维度', [])[:4]:
        print(f"• {dim}")

    print("\n【核心支柱】")
    for pillar in framework.get('核心支柱', [])[:3]:
        print(f"→ {pillar.get('标题', '')} (重要性: {pillar.get('重要性', '')})")

    print("\n【知识层次】")
    hierarchy = framework.get('知识层次', {})
    print(f"总层数: {hierarchy.get('总层数', 0)}")
    print(f"平均每层节点: {hierarchy.get('平均每层节点数', 0):.1f}个")

    print("\n【对称性分析】")
    symmetry = framework.get('对称性分析', {})
    print(f"分支数量: {symmetry.get('分支数量', 0)}")
    print(f"平衡度: {symmetry.get('平衡度', '未知')}")


def demo_daily_report():
    """演示：每日报告"""
    print("\n" + "="*60)
    print("演示5: 每日生活报告")
    print("="*60 + "\n")

    reporter = DailyReporter()

    # 模拟今日数据
    mood_data = {
        "morning": "积极",
        "afternoon": "专注",
        "evening": "满足"
    }

    input_data = {
        "articles": ["AI技术文章", "个人成长文章", "产品设计案例"],
        "videos": ["技术演讲", "TED演讲"],
        "books": ["《深度工作》第5章"]
    }

    activities = [
        "晨间冥想",
        "深度工作2小时",
        "团队会议",
        "学习新技能1小时",
        "运动30分钟",
        "阅读1小时"
    ]

    print("正在分析今日数据...\n")
    report = reporter.generate_daily_report(
        mood_data=mood_data,
        input_data=input_data,
        activities=activities
    )

    print(f"日期: {report.date}\n")

    print("【情绪分析】")
    mood = report.mood_analysis
    print(f"整体状态: {mood.get('整体状态', '')}")
    print(f"情绪趋势: {mood.get('情绪趋势', '')}")
    print(f"积极占比: {mood.get('积极情绪占比', '')}\n")

    print("【大脑总结】")
    print(report.brain_summary[:200] + "...\n")

    print("【成长洞察】")
    for i, insight in enumerate(report.growth_insights[:2], 1):
        print(f"{i}. {insight}\n")

    print("【明日建议】")
    for suggestion in report.tomorrow_suggestions[:3]:
        print(f"{suggestion}")

    print("\n【今日指标】")
    for metric, score in report.metrics.items():
        bar = "█" * int(score) + "░" * (10 - int(score))
        print(f"{metric:12s}: {bar} {score}/10")


def demo_self_improvement():
    """演示：自我提升方案"""
    print("\n" + "="*60)
    print("演示6: 自我提升方案")
    print("="*60 + "\n")

    profile = PersonProfile(
        name="成长者",
        age=27,
        current_career="设计师",
        education="本科",
        skills=["UI设计", "用户体验"],
        interests=["心理学", "技术", "创意"],
        goals=["全方位提升"],
        constraints=[]
    )

    planner = LifePlanner()
    focus_areas = ["技能提升", "思维成长", "健康管理"]

    print(f"关注领域: {', '.join(focus_areas)}\n")
    print("正在生成提升方案...\n")

    plan = planner.create_self_improvement_plan(
        profile=profile,
        focus_areas=focus_areas
    )

    print("【当前状态评估】")
    assessment = plan['assessment']
    print(f"优势: {', '.join(assessment['strengths'][:3])}")
    print(f"待提升: {', '.join(assessment['improvement_areas'])}\n")

    print("【日常实践（前5项）】")
    for practice in plan['daily_practices'][:5]:
        print(f"{practice['time']}: {practice['activity']}")

    print("\n【月度目标】")
    for goal in plan['monthly_goals'][:2]:
        print(f"\n{goal['area']}:")
        print(f"  目标: {goal['goal']}")
        print(f"  指标: {', '.join(goal['metrics'][:2])}")


def main():
    """运行所有演示"""
    print("\n" + "╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  🌟 人生实验仿真引擎 - 功能演示 🌟  ".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")

    demos = [
        ("人生路径模拟", demo_life_simulation),
        ("生活规划", demo_life_planning),
        ("习惯系统", demo_habit_system),
        ("知识图谱", demo_knowledge_graph),
        ("每日报告", demo_daily_report),
        ("自我提升", demo_self_improvement)
    ]

    for i, (name, demo_func) in enumerate(demos, 1):
        print(f"\n\n{'='*60}")
        print(f"即将运行: {name} ({i}/{len(demos)})")
        print(f"{'='*60}")

        try:
            demo_func()
        except Exception as e:
            print(f"\n❌ 演示出错: {e}")

        if i < len(demos):
            input("\n按 Enter 继续下一个演示...")

    print("\n\n" + "="*60)
    print("✅ 所有演示完成！")
    print("="*60)
    print("\n💡 提示:")
    print("- 运行 'python main.py' 开始交互式使用")
    print("- 查看 EXAMPLES.md 获取更多使用示例")
    print("- 查看 README.md 了解完整功能")
    print("\n🚀 开始探索你的无限可能吧！\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 演示已退出！\n")
    except Exception as e:
        print(f"\n❌ 错误: {e}\n")
