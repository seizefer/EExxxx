"""
生活自动报告系统 - 每日分析与建议
"""
from typing import List, Dict, Any
from models import DailyReport
from utils import format_date
import random


class DailyReporter:
    """每日报告生成器"""

    def __init__(self):
        self.report_history = []

    def generate_daily_report(
        self,
        date: str = None,
        mood_data: Dict[str, Any] = None,
        input_data: Dict[str, List[str]] = None,
        activities: List[str] = None
    ) -> DailyReport:
        """
        生成每日报告

        Args:
            date: 日期
            mood_data: 心情数据
            input_data: 输入信息（文章、视频、聊天等）
            activities: 当日活动列表
        """
        report_date = date or format_date()

        # 分析心情
        mood_analysis = self._analyze_mood(mood_data or {})

        # 汇总输入信息
        input_summary = self._summarize_inputs(input_data or {})

        # 生成大脑总结
        brain_summary = self._generate_brain_summary(mood_analysis, input_summary, activities or [])

        # 生成成长洞察
        growth_insights = self._generate_growth_insights(mood_analysis, input_summary, activities or [])

        # 生成明日建议
        tomorrow_suggestions = self._generate_tomorrow_suggestions(mood_analysis, growth_insights)

        # 计算指标
        metrics = self._calculate_daily_metrics(mood_analysis, input_summary, activities or [])

        report = DailyReport(
            date=report_date,
            mood_analysis=mood_analysis,
            input_summary=input_summary,
            brain_summary=brain_summary,
            growth_insights=growth_insights,
            tomorrow_suggestions=tomorrow_suggestions,
            metrics=metrics
        )

        self.report_history.append(report)

        return report

    def _analyze_mood(self, mood_data: Dict[str, Any]) -> Dict[str, Any]:
        """分析心情"""
        # 如果没有提供数据，使用示例数据
        if not mood_data:
            mood_data = {
                "morning": random.choice(["平静", "积极", "疲惫", "焦虑"]),
                "afternoon": random.choice(["专注", "疲惫", "充实", "分心"]),
                "evening": random.choice(["放松", "疲惫", "满足", "焦虑"])
            }

        # 分析整体情绪状态
        moods = list(mood_data.values())
        positive_moods = ["平静", "积极", "专注", "充实", "放松", "满足"]
        negative_moods = ["疲惫", "焦虑", "分心"]

        positive_count = sum(1 for m in moods if m in positive_moods)
        negative_count = sum(1 for m in moods if m in negative_moods)

        if positive_count > negative_count:
            overall_state = "整体积极"
            trend = "上升"
        elif positive_count < negative_count:
            overall_state = "需要关注"
            trend = "下降"
        else:
            overall_state = "基本稳定"
            trend = "持平"

        analysis = {
            "时段情绪": mood_data,
            "整体状态": overall_state,
            "情绪趋势": trend,
            "积极情绪占比": f"{positive_count/len(moods)*100:.0f}%",
            "关注点": self._identify_mood_concerns(mood_data),
            "情绪模式": self._identify_mood_pattern(mood_data)
        }

        return analysis

    def _identify_mood_concerns(self, mood_data: Dict[str, Any]) -> List[str]:
        """识别情绪关注点"""
        concerns = []

        if "焦虑" in str(mood_data.values()):
            concerns.append("检测到焦虑情绪，需要放松和减压")

        if list(mood_data.values()).count("疲惫") >= 2:
            concerns.append("多个时段疲惫，需要调整作息和休息")

        if "分心" in str(mood_data.values()):
            concerns.append("注意力分散，需要优化专注度")

        if not concerns:
            concerns.append("情绪状态良好，继续保持")

        return concerns

    def _identify_mood_pattern(self, mood_data: Dict[str, Any]) -> str:
        """识别情绪模式"""
        patterns = {
            ("积极", "专注", "满足"): "高效能模式 - 状态最佳",
            ("平静", "专注", "放松"): "稳定产出模式 - 可持续",
            ("疲惫", "疲惫", "疲惫"): "耗竭模式 - 需要恢复",
            ("焦虑", "分心", "焦虑"): "压力模式 - 需要调节"
        }

        mood_tuple = tuple(mood_data.values())
        for pattern, description in patterns.items():
            if mood_tuple == pattern:
                return description

        # 默认模式识别
        if "积极" in mood_tuple or "专注" in mood_tuple:
            return "正常波动模式 - 整体向好"
        else:
            return "普通日常模式 - 可优化空间"

    def _summarize_inputs(self, input_data: Dict[str, List[str]]) -> Dict[str, List[str]]:
        """汇总输入信息"""
        if not input_data:
            input_data = {
                "articles": ["科技新闻3篇", "个人成长文章2篇"],
                "videos": ["TED演讲1个", "技术教程2个"],
                "conversations": ["团队会议", "朋友交流"],
                "books": ["《深度工作》第3章"]
            }

        # 为每个类别添加统计
        summary = {}
        for category, items in input_data.items():
            summary[category] = items
            summary[f"{category}_count"] = [f"共{len(items)}项"]

        # 添加主题分析
        summary["主题分布"] = self._analyze_input_themes(input_data)

        # 添加质量评估
        summary["质量评估"] = self._assess_input_quality(input_data)

        return summary

    def _analyze_input_themes(self, input_data: Dict[str, List[str]]) -> List[str]:
        """分析输入主题"""
        themes = []

        all_content = []
        for items in input_data.values():
            if isinstance(items, list):
                all_content.extend(items)

        content_str = " ".join(all_content).lower()

        theme_keywords = {
            "技术": ["技术", "编程", "AI", "算法", "代码"],
            "个人成长": ["成长", "提升", "习惯", "目标"],
            "商业": ["商业", "管理", "创业", "市场"],
            "健康": ["健康", "运动", "健身", "营养"],
            "创意": ["创意", "设计", "艺术", "创新"]
        }

        for theme, keywords in theme_keywords.items():
            if any(kw in content_str for kw in keywords):
                themes.append(theme)

        return themes if themes else ["综合性内容"]

    def _assess_input_quality(self, input_data: Dict[str, List[str]]) -> str:
        """评估输入质量"""
        total_items = sum(len(items) if isinstance(items, list) else 0 for items in input_data.values())

        if total_items >= 8:
            return "高质量输入 - 信息丰富且多样化"
        elif total_items >= 4:
            return "良好输入 - 保持平衡"
        else:
            return "可增加 - 适当扩大信息摄入"

    def _generate_brain_summary(
        self,
        mood_analysis: Dict[str, Any],
        input_summary: Dict[str, List[str]],
        activities: List[str]
    ) -> str:
        """生成今日大脑总结"""
        # 提取关键信息
        overall_mood = mood_analysis.get("整体状态", "基本稳定")
        themes = input_summary.get("主题分布", ["综合"])
        activity_count = len(activities)

        summary = f"""
【今日大脑总结】

情绪状态：{overall_mood}
主要关注：{', '.join(themes[:3])}
活动密度：{activity_count}项活动

核心收获：
1. 在{themes[0] if themes else '各个'}领域有新的认知输入
2. 情绪模式呈现{mood_analysis.get('情绪趋势', '正常')}趋势
3. 大脑处理了多维度的信息和体验

认知负荷：{'适中' if activity_count < 8 else '较高' if activity_count < 12 else '超负荷'}
今日效能：{self._calculate_effectiveness(mood_analysis, activity_count)}

总体评价：今天是{self._generate_day_rating(mood_analysis, input_summary)}的一天。
        """.strip()

        return summary

    def _calculate_effectiveness(self, mood_analysis: Dict[str, Any], activity_count: int) -> str:
        """计算效能"""
        mood_score = 0.8 if mood_analysis.get("整体状态") == "整体积极" else 0.5
        activity_score = min(1.0, activity_count / 10)

        effectiveness = (mood_score + activity_score) / 2

        if effectiveness >= 0.75:
            return "高效能 ⭐⭐⭐"
        elif effectiveness >= 0.5:
            return "中效能 ⭐⭐"
        else:
            return "低效能 ⭐"

    def _generate_day_rating(self, mood_analysis: Dict[str, Any], input_summary: Dict[str, Any]) -> str:
        """生成日期评级"""
        ratings = []

        if mood_analysis.get("整体状态") == "整体积极":
            ratings.append("充实")

        if input_summary.get("质量评估", "").startswith("高质量"):
            ratings.append("有收获")

        if mood_analysis.get("情绪趋势") == "上升":
            ratings.append("向上")

        return "、".join(ratings) if ratings else "平凡但有意义"

    def _generate_growth_insights(
        self,
        mood_analysis: Dict[str, Any],
        input_summary: Dict[str, List[str]],
        activities: List[str]
    ) -> List[str]:
        """生成成长洞察"""
        insights = []

        # 基于情绪的洞察
        if mood_analysis.get("整体状态") == "整体积极":
            insights.append(
                "情绪状态良好，这是深度工作和学习的最佳时期，建议明天继续保持这种状态"
            )
        elif mood_analysis.get("整体状态") == "需要关注":
            insights.append(
                "情绪需要调节，可能是因为休息不足或压力过大，建议明天增加放松时间"
            )

        # 基于输入的洞察
        themes = input_summary.get("主题分布", [])
        if len(themes) >= 3:
            insights.append(
                f"今天涉及{len(themes)}个不同主题，知识面广但可能缺乏深度，"
                "建议下周选择1-2个主题深入研究"
            )
        elif len(themes) == 1:
            insights.append(
                f"今天专注于{themes[0]}领域，深度学习效果好，"
                "可以考虑定期进行这种单一主题的深度日"
            )

        # 基于活动的洞察
        if len(activities) > 10:
            insights.append(
                "今天活动较多，可能导致注意力分散，"
                "建议明天减少任务切换，增加深度工作时间"
            )

        # 模式识别洞察
        pattern = mood_analysis.get("情绪模式", "")
        if "高效能" in pattern:
            insights.append(
                "今天的情绪模式非常理想，回顾一下今天的作息和活动安排，"
                "尝试将这种模式复制到其他日子"
            )

        # 如果洞察不足，添加通用洞察
        if len(insights) < 3:
            insights.extend([
                "持续记录和反思是成长的关键，坚持这个习惯",
                "关注长期趋势比单日表现更重要",
                "每天都是学习和改进的机会"
            ])

        return insights[:4]  # 最多返回4条洞察

    def _generate_tomorrow_suggestions(
        self,
        mood_analysis: Dict[str, Any],
        growth_insights: List[str]
    ) -> List[str]:
        """生成明日建议"""
        suggestions = []

        # 基于情绪的建议
        concerns = mood_analysis.get("关注点", [])
        if any("焦虑" in c for c in concerns):
            suggestions.append("🧘 早晨增加10分钟冥想或深呼吸练习")
            suggestions.append("📝 列出让你焦虑的具体事项，逐一制定应对方案")

        if any("疲惫" in c for c in concerns):
            suggestions.append("😴 今晚提前30分钟睡觉，确保7-8小时睡眠")
            suggestions.append("⚡ 明天减少30%的任务量，给自己恢复空间")

        if any("分心" in c for c in concerns):
            suggestions.append("🎯 使用番茄工作法，25分钟专注+5分钟休息")
            suggestions.append("📵 工作时段关闭手机通知和社交媒体")

        # 如果情绪良好，提供提升建议
        if mood_analysis.get("整体状态") == "整体积极":
            suggestions.append("🚀 趁状态好，明天安排一个挑战性任务")
            suggestions.append("📚 增加30分钟深度学习时间")

        # 通用建议
        general_suggestions = [
            "🌅 早晨花5分钟设定今天的3个最重要目标",
            "💧 确保全天饮水2000ml以上",
            "🏃 至少30分钟的身体活动",
            "🌙 睡前30分钟远离屏幕，进行放松活动",
            "🙏 每天记录3件感恩的事",
            "📖 阅读30分钟有价值的内容",
            "🤝 与至少一个人进行有意义的交流"
        ]

        # 随机添加1-2个通用建议
        suggestions.extend(random.sample(general_suggestions, min(2, 7 - len(suggestions))))

        return suggestions[:7]  # 最多7条建议

    def _calculate_daily_metrics(
        self,
        mood_analysis: Dict[str, Any],
        input_summary: Dict[str, List[str]],
        activities: List[str]
    ) -> Dict[str, float]:
        """计算每日指标"""
        # 情绪分数
        mood_score = 0.8 if mood_analysis.get("整体状态") == "整体积极" else \
                     0.5 if mood_analysis.get("整体状态") == "基本稳定" else 0.3

        # 学习输入分数
        total_inputs = sum(
            len(v) if isinstance(v, list) else 0
            for k, v in input_summary.items()
            if not k.endswith("_count") and k not in ["主题分布", "质量评估"]
        )
        learning_score = min(1.0, total_inputs / 8)

        # 活动丰富度
        activity_score = min(1.0, len(activities) / 10) if activities else 0.5

        # 平衡度（基于主题多样性）
        themes = input_summary.get("主题分布", [])
        balance_score = min(1.0, len(themes) / 4)

        # 综合成长分数
        growth_score = (mood_score * 0.3 + learning_score * 0.4 +
                       activity_score * 0.2 + balance_score * 0.1)

        metrics = {
            "情绪分数": round(mood_score * 10, 1),
            "学习输入": round(learning_score * 10, 1),
            "活动丰富度": round(activity_score * 10, 1),
            "生活平衡度": round(balance_score * 10, 1),
            "综合成长分数": round(growth_score * 10, 1)
        }

        return metrics

    def generate_weekly_summary(self, days: int = 7) -> Dict[str, Any]:
        """生成周度总结"""
        if len(self.report_history) < days:
            return {
                "message": f"需要至少{days}天的数据才能生成周度总结",
                "current_days": len(self.report_history)
            }

        recent_reports = self.report_history[-days:]

        summary = {
            "周期": f"最近{days}天",
            "情绪趋势": self._analyze_mood_trend(recent_reports),
            "成长轨迹": self._analyze_growth_trajectory(recent_reports),
            "主题分布": self._analyze_weekly_themes(recent_reports),
            "平均指标": self._calculate_average_metrics(recent_reports),
            "亮点时刻": self._identify_highlights(recent_reports),
            "改进建议": self._generate_weekly_recommendations(recent_reports)
        }

        return summary

    def _analyze_mood_trend(self, reports: List[DailyReport]) -> Dict[str, Any]:
        """分析情绪趋势"""
        positive_days = sum(
            1 for r in reports
            if r.mood_analysis.get("整体状态") == "整体积极"
        )

        return {
            "积极天数": f"{positive_days}/{len(reports)}",
            "积极率": f"{positive_days/len(reports)*100:.0f}%",
            "趋势": "上升" if positive_days > len(reports) / 2 else "需改善"
        }

    def _analyze_growth_trajectory(self, reports: List[DailyReport]) -> Dict[str, Any]:
        """分析成长轨迹"""
        growth_scores = [r.metrics.get("综合成长分数", 5) for r in reports]

        return {
            "平均成长分数": f"{sum(growth_scores)/len(growth_scores):.1f}/10",
            "最高分": f"{max(growth_scores):.1f}",
            "最低分": f"{min(growth_scores):.1f}",
            "波动性": "稳定" if max(growth_scores) - min(growth_scores) < 3 else "波动较大"
        }

    def _analyze_weekly_themes(self, reports: List[DailyReport]) -> List[str]:
        """分析周度主题"""
        all_themes = []

        for report in reports:
            themes = report.input_summary.get("主题分布", [])
            all_themes.extend(themes)

        # 统计频率
        theme_freq = {}
        for theme in all_themes:
            theme_freq[theme] = theme_freq.get(theme, 0) + 1

        sorted_themes = sorted(theme_freq.items(), key=lambda x: x[1], reverse=True)

        return [f"{theme} ({count}天)" for theme, count in sorted_themes[:5]]

    def _calculate_average_metrics(self, reports: List[DailyReport]) -> Dict[str, float]:
        """计算平均指标"""
        metrics_sum = {}
        metric_keys = ["情绪分数", "学习输入", "活动丰富度", "生活平衡度", "综合成长分数"]

        for key in metric_keys:
            values = [r.metrics.get(key, 0) for r in reports]
            metrics_sum[key] = round(sum(values) / len(values), 1)

        return metrics_sum

    def _identify_highlights(self, reports: List[DailyReport]) -> List[str]:
        """识别亮点时刻"""
        highlights = []

        # 找出最高成长分数的一天
        best_day = max(reports, key=lambda r: r.metrics.get("综合成长分数", 0))
        highlights.append(
            f"{best_day.date}: 最佳表现日 "
            f"(成长分数 {best_day.metrics.get('综合成长分数', 0)}/10)"
        )

        # 找出持续积极的天数
        consecutive_positive = 0
        max_consecutive = 0

        for report in reports:
            if report.mood_analysis.get("整体状态") == "整体积极":
                consecutive_positive += 1
                max_consecutive = max(max_consecutive, consecutive_positive)
            else:
                consecutive_positive = 0

        if max_consecutive >= 3:
            highlights.append(f"连续{max_consecutive}天保持积极状态")

        return highlights

    def _generate_weekly_recommendations(self, reports: List[DailyReport]) -> List[str]:
        """生成周度建议"""
        recommendations = []

        # 基于情绪趋势
        mood_trend = self._analyze_mood_trend(reports)
        if "需改善" in mood_trend.get("趋势", ""):
            recommendations.append(
                "本周情绪状态需要关注，建议增加休息和放松活动"
            )

        # 基于成长轨迹
        growth_trajectory = self._analyze_growth_trajectory(reports)
        if "波动较大" in growth_trajectory.get("波动性", ""):
            recommendations.append(
                "成长分数波动较大，建议建立更稳定的日常节奏"
            )

        # 基于平均指标
        avg_metrics = self._calculate_average_metrics(reports)
        if avg_metrics.get("学习输入", 0) < 6:
            recommendations.append(
                "学习输入偏低，下周增加高质量内容的摄入"
            )

        if avg_metrics.get("生活平衡度", 0) < 6:
            recommendations.append(
                "生活领域需要更多元化，尝试探索新的主题和活动"
            )

        # 通用建议
        if not recommendations:
            recommendations.append("整体表现良好，继续保持当前节奏")

        return recommendations
