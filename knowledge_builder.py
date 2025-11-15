"""
知识体系建立 - 多层知识图谱构建
"""
from typing import List, Dict, Any
from models import KnowledgeGraph, KnowledgeNode
from utils import generate_id
import random


class KnowledgeBuilder:
    """知识体系构建器"""

    def __init__(self):
        self.max_depth = 20
        self.nodes_per_level = {}

    def build_knowledge_graph(
        self,
        topic: str,
        depth: int = 20,
        breadth: str = "medium"
    ) -> KnowledgeGraph:
        """
        构建知识图谱

        Args:
            topic: 主题
            depth: 深度（层数）
            breadth: 广度（narrow/medium/wide）
        """
        graph = KnowledgeGraph(
            topic=topic,
            max_depth=depth
        )

        # 生成多层知识节点
        nodes = self._generate_hierarchical_nodes(topic, depth, breadth)
        graph.nodes = nodes
        graph.total_concepts = len(nodes)

        # 建立节点连接
        self._establish_connections(graph)

        # 生成抽象框架
        graph.framework = self._build_abstract_framework(graph)

        return graph

    def _generate_hierarchical_nodes(
        self,
        topic: str,
        depth: int,
        breadth: str
    ) -> List[KnowledgeNode]:
        """生成分层知识节点"""
        nodes = []
        breadth_factor = {"narrow": 2, "medium": 3, "wide": 5}.get(breadth, 3)

        # 第0层：主题根节点
        root_node = KnowledgeNode(
            node_id=generate_id("node_0_"),
            title=topic,
            level=0,
            content=self._generate_topic_overview(topic),
            concepts=self._extract_core_concepts(topic),
            importance_score=1.0
        )
        nodes.append(root_node)

        # 生成各层节点
        parent_nodes = [root_node]

        for level in range(1, depth + 1):
            current_level_nodes = []

            for parent in parent_nodes:
                # 每个父节点生成多个子节点
                num_children = breadth_factor if level < 5 else max(1, breadth_factor - 1)

                for i in range(num_children):
                    child_node = self._create_child_node(parent, level, i)
                    nodes.append(child_node)
                    current_level_nodes.append(child_node)

            parent_nodes = current_level_nodes

            # 控制扩展，避免节点过多
            if level > 10 and len(parent_nodes) > 20:
                parent_nodes = random.sample(parent_nodes, 20)

        return nodes

    def _create_child_node(
        self,
        parent: KnowledgeNode,
        level: int,
        index: int
    ) -> KnowledgeNode:
        """创建子节点"""
        # 根据父节点和层级生成子主题
        subtopics = self._generate_subtopics(parent.title, level)

        if index < len(subtopics):
            title = subtopics[index]
        else:
            title = f"{parent.title} - 扩展主题{index + 1}"

        # 计算重要性分数（越深层越低）
        importance_score = max(0.1, 1.0 - (level * 0.04))

        node = KnowledgeNode(
            node_id=generate_id(f"node_{level}_"),
            title=title,
            level=level,
            content=self._generate_node_content(title, level),
            concepts=self._generate_concepts(title, level),
            importance_score=importance_score
        )

        # 建立与父节点的连接
        node.connections.append(parent.node_id)

        return node

    def _generate_topic_overview(self, topic: str) -> str:
        """生成主题概述"""
        overviews = {
            "人工智能史": """
人工智能的发展历程可以追溯到1950年代，经历了多次繁荣与寒冬。
从早期的符号主义到现代的深度学习，AI领域不断演进和突破。
主要里程碑包括：图灵测试(1950)、感知机(1958)、专家系统(1970s)、
神经网络复兴(1980s)、深度学习革命(2010s)等。
            """,
            "人类心理结构": """
人类心理结构包括认知、情感、意志三大系统。
认知系统处理信息和知识，情感系统产生情绪和感受，
意志系统负责决策和行动。这三个系统相互作用，
构成了完整的心理活动框架。现代心理学从生理、认知、
社会等多个角度研究人类心理的复杂机制。
            """,
            "行为经济学": """
行为经济学整合了心理学和经济学，研究人类在经济决策中的
非理性行为。传统经济学假设人是理性的，但行为经济学发现
人类决策受到认知偏差、情绪、社会因素等多重影响。
核心概念包括：有限理性、启发式思维、框架效应、损失厌恶等。
            """,
            "佛教哲学": """
佛教哲学以"苦、集、灭、道"四谛为核心，探讨人生痛苦的本质、
起源、消除和方法。核心思想包括缘起性空、无常、无我、中道等。
佛教不仅是宗教，更是一套完整的哲学体系和实践方法，
对东方文化和思想产生了深远影响。
            """
        }

        return overviews.get(topic, f"""
{topic}是一个复杂而深刻的知识领域，涉及多个维度和层面。
通过系统性的学习和理解，我们可以建立对{topic}的完整认知框架。
这个主题包含了理论基础、历史发展、核心概念、实践应用等多个方面。
        """).strip()

    def _extract_core_concepts(self, topic: str) -> List[str]:
        """提取核心概念"""
        concept_map = {
            "人工智能史": ["图灵测试", "机器学习", "深度学习", "神经网络", "符号主义", "专家系统"],
            "人类心理结构": ["认知系统", "情感系统", "意志系统", "意识", "潜意识", "人格"],
            "行为经济学": ["有限理性", "启发式", "框架效应", "损失厌恶", "锚定效应", "心理账户"],
            "佛教哲学": ["四谛", "八正道", "缘起", "空性", "无常", "无我", "中道"]
        }

        return concept_map.get(topic, [
            f"{topic}核心概念1",
            f"{topic}核心概念2",
            f"{topic}核心概念3"
        ])

    def _generate_subtopics(self, parent_title: str, level: int) -> List[str]:
        """生成子主题"""
        # 根据父主题和层级生成相关子主题
        if "人工智能" in parent_title:
            if level == 1:
                return ["AI的起源与早期发展", "机器学习的兴起", "深度学习革命", "AI应用领域", "AI伦理与未来"]
            elif level == 2:
                if "起源" in parent_title:
                    return ["图灵与计算理论", "达特茅斯会议", "早期AI研究"]
                elif "机器学习" in parent_title:
                    return ["监督学习", "无监督学习", "强化学习"]
                elif "深度学习" in parent_title:
                    return ["卷积神经网络", "循环神经网络", "Transformer架构"]

        elif "心理" in parent_title:
            if level == 1:
                return ["认知心理学", "情感心理学", "发展心理学", "社会心理学", "神经心理学"]
            elif level == 2:
                if "认知" in parent_title:
                    return ["注意力", "记忆", "思维", "语言", "问题解决"]
                elif "情感" in parent_title:
                    return ["情绪理论", "情绪调节", "情绪智力"]

        elif "行为经济学" in parent_title:
            if level == 1:
                return ["认知偏差", "决策理论", "风险与不确定性", "社会影响", "市场行为"]
            elif level == 2:
                if "认知偏差" in parent_title:
                    return ["确认偏差", "可得性启发", "代表性启发", "锚定效应"]
                elif "决策" in parent_title:
                    return ["前景理论", "期望效用", "损失厌恶"]

        elif "佛教" in parent_title:
            if level == 1:
                return ["基本教义", "修行方法", "佛教宗派", "佛教哲学思想", "佛教与现代社会"]
            elif level == 2:
                if "教义" in parent_title:
                    return ["四谛", "八正道", "十二因缘", "三法印"]
                elif "修行" in parent_title:
                    return ["戒定慧", "禅修方法", "念佛法门"]

        # 通用子主题生成
        return [
            f"{parent_title} - 理论基础",
            f"{parent_title} - 核心概念",
            f"{parent_title} - 实践应用"
        ]

    def _generate_node_content(self, title: str, level: int) -> str:
        """生成节点内容"""
        # 根据层级调整内容详细度
        if level <= 3:
            detail = "深入"
        elif level <= 10:
            detail = "中等"
        else:
            detail = "简要"

        return f"""
【{title}】

这是关于{title}的{detail}介绍。在知识体系的第{level}层，
此节点代表了该主题的一个重要方面。

核心要点：
- 定义与背景
- 关键特征
- 重要性与应用
- 与其他概念的关联

通过理解{title}，我们可以更全面地把握整个知识领域。
        """.strip()

    def _generate_concepts(self, title: str, level: int) -> List[str]:
        """生成概念列表"""
        num_concepts = max(1, 5 - level // 4)  # 越深层概念越少

        concepts = []
        for i in range(num_concepts):
            concepts.append(f"{title}的概念{i + 1}")

        return concepts

    def _establish_connections(self, graph: KnowledgeGraph) -> None:
        """建立节点间的连接"""
        nodes_by_level = {}

        # 按层级组织节点
        for node in graph.nodes:
            if node.level not in nodes_by_level:
                nodes_by_level[node.level] = []
            nodes_by_level[node.level].append(node)

        # 在同层节点间建立横向连接
        for level, nodes in nodes_by_level.items():
            for i, node in enumerate(nodes):
                # 连接到同层的相邻节点
                if i < len(nodes) - 1:
                    neighbor = nodes[i + 1]
                    if neighbor.node_id not in node.connections:
                        node.connections.append(neighbor.node_id)

                # 随机建立跨层连接
                if level > 0 and random.random() > 0.7:
                    if level - 1 in nodes_by_level:
                        parent_level_nodes = nodes_by_level[level - 1]
                        random_parent = random.choice(parent_level_nodes)
                        if random_parent.node_id not in node.connections:
                            node.connections.append(random_parent.node_id)

    def _build_abstract_framework(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        """构建抽象框架"""
        framework = {
            "主题": graph.topic,
            "知识维度": self._identify_dimensions(graph),
            "核心支柱": self._identify_pillars(graph),
            "关键概念": self._extract_key_concepts(graph),
            "知识层次": self._analyze_hierarchy(graph),
            "对称性分析": self._analyze_symmetry(graph),
            "知识密度": self._calculate_density(graph)
        }

        return framework

    def _identify_dimensions(self, graph: KnowledgeGraph) -> List[str]:
        """识别知识维度"""
        # 分析第一层节点的主题类别
        first_level_nodes = [n for n in graph.nodes if n.level == 1]

        dimensions = []
        for node in first_level_nodes[:6]:  # 最多6个主要维度
            dimensions.append(node.title)

        return dimensions

    def _identify_pillars(self, graph: KnowledgeGraph) -> List[Dict[str, Any]]:
        """识别核心支柱"""
        # 找出最重要的节点作为支柱
        sorted_nodes = sorted(
            graph.nodes,
            key=lambda n: n.importance_score,
            reverse=True
        )

        pillars = []
        for node in sorted_nodes[:5]:
            pillars.append({
                "标题": node.title,
                "层级": node.level,
                "重要性": f"{node.importance_score:.2f}",
                "核心概念": node.concepts[:3]
            })

        return pillars

    def _extract_key_concepts(self, graph: KnowledgeGraph) -> List[str]:
        """提取关键概念"""
        all_concepts = []

        for node in graph.nodes:
            all_concepts.extend(node.concepts)

        # 统计频率并返回最常见的概念
        concept_freq = {}
        for concept in all_concepts:
            concept_freq[concept] = concept_freq.get(concept, 0) + 1

        sorted_concepts = sorted(
            concept_freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return [concept for concept, _ in sorted_concepts[:15]]

    def _analyze_hierarchy(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        """分析层次结构"""
        levels_distribution = {}

        for node in graph.nodes:
            level = node.level
            levels_distribution[level] = levels_distribution.get(level, 0) + 1

        return {
            "总层数": graph.max_depth,
            "总节点数": len(graph.nodes),
            "层次分布": levels_distribution,
            "平均每层节点数": len(graph.nodes) / (graph.max_depth + 1),
            "最深层节点": max(n.level for n in graph.nodes)
        }

    def _analyze_symmetry(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        """对称性分析"""
        # 分析知识结构的对称性和平衡性
        first_level = [n for n in graph.nodes if n.level == 1]

        # 分析各分支的深度
        branch_depths = {}
        for node in first_level:
            branch_depths[node.title] = self._calculate_branch_depth(node, graph)

        return {
            "分支数量": len(first_level),
            "分支深度": branch_depths,
            "平衡度": self._calculate_balance(branch_depths),
            "对称性评分": self._calculate_symmetry_score(branch_depths)
        }

    def _calculate_branch_depth(self, root: KnowledgeNode, graph: KnowledgeGraph) -> int:
        """计算分支深度"""
        max_depth = root.level

        # 找到所有后代节点
        descendants = [n for n in graph.nodes if root.node_id in n.connections]

        for desc in descendants:
            desc_depth = self._calculate_branch_depth(desc, graph)
            max_depth = max(max_depth, desc_depth)

        return max_depth

    def _calculate_balance(self, branch_depths: Dict[str, int]) -> str:
        """计算平衡度"""
        if not branch_depths:
            return "无法评估"

        depths = list(branch_depths.values())
        avg_depth = sum(depths) / len(depths)
        max_deviation = max(abs(d - avg_depth) for d in depths)

        if max_deviation < 2:
            return "高度平衡"
        elif max_deviation < 4:
            return "基本平衡"
        else:
            return "不平衡"

    def _calculate_symmetry_score(self, branch_depths: Dict[str, int]) -> float:
        """计算对称性评分"""
        if not branch_depths:
            return 0.0

        depths = list(branch_depths.values())
        if len(depths) == 1:
            return 1.0

        avg_depth = sum(depths) / len(depths)
        variance = sum((d - avg_depth) ** 2 for d in depths) / len(depths)

        # 方差越小，对称性越高
        symmetry_score = max(0, 1 - (variance / 10))

        return symmetry_score

    def _calculate_density(self, graph: KnowledgeGraph) -> Dict[str, Any]:
        """计算知识密度"""
        total_connections = sum(len(n.connections) for n in graph.nodes)
        total_concepts = sum(len(n.concepts) for n in graph.nodes)

        return {
            "节点密度": len(graph.nodes) / (graph.max_depth + 1),
            "连接密度": total_connections / len(graph.nodes) if graph.nodes else 0,
            "概念密度": total_concepts / len(graph.nodes) if graph.nodes else 0,
            "平均概念数": total_concepts / len(graph.nodes) if graph.nodes else 0
        }

    def perform_cross_literature_reasoning(
        self,
        graph: KnowledgeGraph,
        perspectives: List[str]
    ) -> Dict[str, Any]:
        """跨文献推理"""
        reasoning = {
            "主题": graph.topic,
            "分析视角": perspectives,
            "交叉发现": [],
            "综合洞察": [],
            "知识整合": {}
        }

        # 从不同视角分析主题
        for perspective in perspectives:
            cross_finding = self._analyze_from_perspective(graph, perspective)
            reasoning["交叉发现"].append(cross_finding)

        # 生成综合洞察
        reasoning["综合洞察"] = self._generate_synthesis(graph, perspectives)

        # 知识整合
        reasoning["知识整合"] = self._integrate_knowledge(graph, perspectives)

        return reasoning

    def _analyze_from_perspective(
        self,
        graph: KnowledgeGraph,
        perspective: str
    ) -> Dict[str, Any]:
        """从特定视角分析"""
        return {
            "视角": perspective,
            "相关节点": [n.title for n in graph.nodes[:5]],
            "核心发现": f"从{perspective}视角看，{graph.topic}呈现出独特的特征",
            "关联概念": [c for n in graph.nodes[:3] for c in n.concepts[:2]]
        }

    def _generate_synthesis(
        self,
        graph: KnowledgeGraph,
        perspectives: List[str]
    ) -> List[str]:
        """生成综合洞察"""
        insights = [
            f"{graph.topic}在{perspectives[0]}和{perspectives[1] if len(perspectives) > 1 else '其他领域'}之间存在深层联系",
            f"通过多视角分析，我们发现{graph.topic}的核心本质是跨学科的",
            f"整合{len(perspectives)}个视角后，对{graph.topic}的理解更加立体和完整",
            f"{graph.topic}的知识结构呈现出{len(graph.nodes)}个关键节点的网络"
        ]

        return insights

    def _integrate_knowledge(
        self,
        graph: KnowledgeGraph,
        perspectives: List[str]
    ) -> Dict[str, List[str]]:
        """整合知识"""
        integration = {}

        for perspective in perspectives:
            integration[perspective] = [
                f"{graph.topic}在{perspective}中的应用",
                f"{perspective}对{graph.topic}的独特贡献",
                f"{graph.topic}与{perspective}的交叉领域"
            ]

        return integration

    def generate_knowledge_book(
        self,
        graph: KnowledgeGraph,
        title: str = None
    ) -> Dict[str, Any]:
        """生成知识电子书"""
        book_title = title or f"{graph.topic}知识手册"

        book = {
            "书名": book_title,
            "目录": self._generate_table_of_contents(graph),
            "章节内容": self._generate_chapters(graph),
            "附录": {
                "核心概念索引": self._generate_concept_index(graph),
                "知识图谱可视化": self._generate_visualization_guide(graph),
                "延伸阅读": self._generate_reading_list(graph.topic)
            },
            "总页数估计": len(graph.nodes) * 2
        }

        return book

    def _generate_table_of_contents(self, graph: KnowledgeGraph) -> List[Dict[str, Any]]:
        """生成目录"""
        toc = []

        # 第一章：概述
        toc.append({
            "章节": "第一章",
            "标题": f"{graph.topic}概述",
            "小节": ["定义与背景", "发展历程", "核心价值"]
        })

        # 后续章节基于第一层节点
        first_level_nodes = sorted(
            [n for n in graph.nodes if n.level == 1],
            key=lambda n: n.importance_score,
            reverse=True
        )

        for i, node in enumerate(first_level_nodes[:8], start=2):
            # 找到该节点的子节点
            children = [n for n in graph.nodes if node.node_id in n.connections and n.level == node.level + 1]

            toc.append({
                "章节": f"第{['一', '二', '三', '四', '五', '六', '七', '八', '九'][i-1] if i <= 9 else i}章",
                "标题": node.title,
                "小节": [child.title for child in children[:5]]
            })

        return toc

    def _generate_chapters(self, graph: KnowledgeGraph) -> List[Dict[str, Any]]:
        """生成章节内容"""
        chapters = []

        # 概述章节
        chapters.append({
            "章节编号": 1,
            "标题": f"{graph.topic}概述",
            "内容": graph.nodes[0].content if graph.nodes else "",
            "关键点": graph.framework.get("核心支柱", [])
        })

        # 其他章节
        first_level_nodes = [n for n in graph.nodes if n.level == 1]

        for i, node in enumerate(first_level_nodes[:8], start=2):
            chapters.append({
                "章节编号": i,
                "标题": node.title,
                "内容": node.content,
                "核心概念": node.concepts,
                "子主题": [n.title for n in graph.nodes if node.node_id in n.connections][:5]
            })

        return chapters

    def _generate_concept_index(self, graph: KnowledgeGraph) -> List[str]:
        """生成概念索引"""
        all_concepts = set()

        for node in graph.nodes:
            all_concepts.update(node.concepts)

        return sorted(list(all_concepts))

    def _generate_visualization_guide(self, graph: KnowledgeGraph) -> Dict[str, str]:
        """生成可视化指南"""
        return {
            "图谱说明": f"本知识图谱包含{len(graph.nodes)}个节点，分为{graph.max_depth + 1}层",
            "阅读建议": "从中心主题开始，逐层向外扩展阅读",
            "重点节点": "标注为红色的节点是核心概念，建议优先学习",
            "连接线": "实线表示直接关联，虚线表示间接关联"
        }

    def _generate_reading_list(self, topic: str) -> List[str]:
        """生成阅读清单"""
        reading_lists = {
            "人工智能史": [
                "《人工智能：一种现代的方法》",
                "《深度学习》(Goodfellow等)",
                "《机器学习》(周志华)",
                "《人工智能简史》"
            ],
            "人类心理结构": [
                "《心理学与生活》",
                "《思考，快与慢》",
                "《认知心理学》",
                "《情绪心理学》"
            ],
            "行为经济学": [
                "《思考，快与慢》",
                "《助推》",
                "《怪诞行为学》",
                "《非理性繁荣》"
            ],
            "佛教哲学": [
                "《金刚经》",
                "《心经》",
                "《佛教哲学》",
                "《禅与摩托车维修艺术》"
            ]
        }

        return reading_lists.get(topic, [
            f"{topic}入门读物",
            f"{topic}进阶教材",
            f"{topic}经典著作"
        ])
