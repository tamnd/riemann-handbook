---
title: Base-change-stable bases of sections
decls:
  - GlobalTheory.AmpleSecBC.secBaseChange_relAmple
  - GlobalTheory.HomFixLocBasis.exists_basicOpen_secBasis
  - GlobalTheory.T.exists_basicOpen_baseChangeStable_sectionBasis
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Base-change-stable bases of sections

The scheme of homomorphisms with fixed pullback of Section 8.8 is built from bases of sections of $L^k$ and $M^k$ that remain bases after every base change (Definition 8.8.4). Section 8.9 needs such bases locally on a noetherian base, as its result 2. This section proves that they exist. The idea is cohomology and base change. Locally on the base, the sections of $L^a$ after any base change are the kernel of one matrix $D_0$. At a point where $H^1$ of the fibre vanishes, this kernel is free and its formation commutes with base change near the point. The previous section gives the vanishing of $H^1$ on every geometric fibre.

### Inputs

We use the following results. Let $R$ be a ring and $X$ a scheme over $\operatorname{Spec} R$.

1. (Projective over an affine open.) Let $A$ be a group scheme over a scheme $S$ with a relatively ample line bundle $L$, and let $t : \operatorname{Spec} R \to S$ be an open immersion. Then $A \times_S \operatorname{Spec} R \to \operatorname{Spec} R$ is very ample in the sense of Definition 8.8.3: some line bundle on it has finitely many sections with the properties listed there.
2. (A complex that computes sections.) Let $R$ be [[noetherian|0670T59HGE]], let $X \to \operatorname{Spec} R$ be [[flat|5M6KS8F47R]] and very ample as in result 1, and let $P$ be a line bundle on $X$. Then there are matrices $D_0 \in R^{b \times a}$ and $D_1 \in R^{c \times b}$ with $D_1 D_0 = 0$ and fixed local sections $u_1, \dots, u_a$ of $P$, with two properties. For every ring map $g : R \to R'$, the map $v \mapsto \sum_k v_k u_k$ is a bijection from $\ker(D_0 \otimes R') \subseteq R'^a$ onto the global sections of $P$ on $X_{R'}$. If also the first cohomology of $P$ on $X_{R'}$ vanishes, then $\ker(D_1 \otimes R') = \operatorname{im}(D_0 \otimes R')$.
3. (A kernel basis near a point.) Let $D_0 \in R^{b \times a}$ and $D_1 \in R^{c \times b}$ with $D_1 D_0 = 0$, and let $g_0 : R \to K$ be a map to a field with $\ker(D_1 \otimes K) = \operatorname{im}(D_0 \otimes K)$. Then there are $r \in R$ with $g_0(r) \neq 0$, an integer $n$ and a matrix $B \in R^{a \times n}$ with $D_0 B = 0$, such that for every ring map $g : R \to R'$ with $g(r)$ a unit, the map $z \mapsto Bz$ is a bijection from $R'^n$ onto $\ker(D_0 \otimes R')$.
4. (Bases from a kernel basis.) In the situation of results 2 and 3, let $X_{R'}$ be the base change along $g$ with $g(r)$ a unit, and let $b_i$ be the section of $P$ on $X_{R'}$ given by the $i$-th column of $B$. Then $b_1, \dots, b_n$ are linearly independent over $R'$ and span the global sections of $P$ on $X_{R'}$.
5. (Geometric points.) For every prime $\mathfrak{q}$ of $R$ there are an algebraically closed field $K$ and $g_0 : R \to K$ with $g_0(\mathfrak{q}) = 0$.
6. (Transfer along an isomorphism.) Let $\varphi : A_g \to A$ and let $h : A_g \times_{S'} \operatorname{Spec} R' \to A \times_S \operatorname{Spec} R'$ be an isomorphism over $\operatorname{Spec} R'$ compatible with $\varphi$. If sections of $L^k$ on the target are a basis, then their pullbacks along $h$ are a basis of the sections of $(\varphi^* L)^k$ on the source.

Result 3 is a statement of linear algebra over $R$. The vanishing $\ker(D_1 \otimes K) = \operatorname{im}(D_0 \otimes K)$ makes $\operatorname{im}(D_0 \otimes K)$ as large as it can be, and the rank of $D_0$ at $g_0$ then spreads to the open set $D(r)$.

### Bases near a point

**Theorem 8.15.1 (Base-change-stable bases near a point).** Let $S$ be a locally noetherian scheme, $A$ an [[abelian scheme|JDDXZ89N33]] over $S$, $L$ a rigidified, relatively ample line bundle on $A$, $a \geq 1$ and $p \in S$. Then there are an open set $V \subseteq S$ with $p \in V$ and sections $b_1, \dots, b_m$ of $L^a$ on $A_V$ with this property. For every ring $R'$ and every $t : \operatorname{Spec} R' \to V$, the pullbacks of $b_1, \dots, b_m$ to $A_{R'}$ are linearly independent over $R'$ and span the global sections of $L^a$ on $A_{R'}$.

Lean: `GlobalTheory.AmpleSecBC.secBaseChange_relAmple`.

*Proof.* Choose an affine open neighbourhood of $p$, with open immersion $t_0 : \operatorname{Spec} R \to S$, and let $\mathfrak{q} \in \operatorname{Spec} R$ map to $p$. As $S$ is locally noetherian, $R$ is noetherian. Put $X = A \times_S \operatorname{Spec} R$. An abelian scheme is [[smooth|EXKGG9X6J0]], so $X \to \operatorname{Spec} R$ is flat, and it is very ample by result 1. Result 2, for $P = L^a$ on $X$, gives $D_0$, $D_1$ and $u_1, \dots, u_a$. Result 5 gives a geometric point $g_0 : R \to K$ with $g_0(\mathfrak{q}) = 0$. By the [corollary on geometric fibres](/entry/geom-vanishing/), the first cohomology of $L^a$ on the fibre $X_K$ vanishes. So $\ker(D_1 \otimes K) = \operatorname{im}(D_0 \otimes K)$ by result 2. Result 3 gives $r \in R$ with $g_0(r) \neq 0$ and a matrix $B$ with $n$ columns.

Each column of $B$ lies in $\ker D_0$. By result 2, for $g = \operatorname{id}_R$, it gives a section $b_{0,i}$ of $L^a$ on $X$. As $g_0(r) \neq 0$ and $g_0(\mathfrak{q}) = 0$, we have $r \notin \mathfrak{q}$, so $\mathfrak{q} \in D(r)$. Let $V = t_0(D(r))$. It is open, since $t_0$ is an open immersion, and $p \in V$. Let $b_i$ be the pullback of $b_{0,i}$ to $A_V$, along the map $V \to \operatorname{Spec} R$ that inverts $t_0$ on $D(r)$. Put $m = n$.

Let $t : \operatorname{Spec} R' \to V$. The composite $\operatorname{Spec} R' \to \operatorname{Spec} R$ lands in $D(r)$, so the image of $r$ in $R'$ is a unit at every point of $\operatorname{Spec} R'$, hence a unit. The pullback of $b_i$ to $A_{R'}$ is the section given by the $i$-th column of $B$, since pullback of sections is compatible with the description of result 2. Result 4 shows that these pullbacks are linearly independent and span. $\square$

The open set $V$ is $D(r)$ inside one affine chart. Its size is controlled by the single element $r$, which the linear algebra of result 3 produces.

**Corollary 8.15.2 (Local bases of sections).** Let $R$ be a noetherian ring, $A$ an abelian scheme over $\operatorname{Spec} R$, $L$ a rigidified, relatively ample line bundle on $A$, $k \geq 1$ and $p \in \operatorname{Spec} R$. Then there is $f \in R$ with $p \in D(f)$ with this property. For every $g \in R$ with $D(g) \subseteq D(f)$ and every group pullback $\varphi : A_g \to A$ along $\operatorname{Spec} R_g \to \operatorname{Spec} R$ (Definition 8.2.5), the line bundle $(\varphi^* L)^k$ on $A_g$ has a base-change-stable basis.

Lean: `GlobalTheory.HomFixLocBasis.exists_basicOpen_secBasis` (also `GlobalTheory.T.exists_basicOpen_baseChangeStable_sectionBasis`, a second name).

*Proof.* The theorem, for $S = \operatorname{Spec} R$ and $a = k$, gives $V \ni p$ and $b_1, \dots, b_m$. The basic open sets form a basis of the topology of $\operatorname{Spec} R$, so there is $f$ with $p \in D(f) \subseteq V$. Let $D(g) \subseteq D(f)$. The image of $\operatorname{Spec} R_g \to \operatorname{Spec} R$ is $D(g)$, which lies in $V$, so this map factors through $V$. Pull the $b_i$ back to sections of $(\varphi^* L)^k$ on $A_g$. Let $t : \operatorname{Spec} R' \to \operatorname{Spec} R_g$, and let $t'$ be its composite with $\operatorname{Spec} R_g \to V$. As $\varphi$ identifies $A_g$ with $A \times \operatorname{Spec} R_g$, the canonical map $A_g \times \operatorname{Spec} R' \to A \times_V \operatorname{Spec} R'$ is an isomorphism. By the theorem, the pullbacks of the $b_i$ along $t'$ form a basis. Result 6 transfers this basis to the pullbacks of the sections on $A_g$ along $t$. $\square$

**Remark 8.15.3 (Formalization).** In the theorem, the rigidification of $L$ is assumed but not used: [IsProjByOfOpenImmersion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProjByOfOpenImmersion.lean#L53). The corollary only passes it on. The base-change-stable basis over $V$ is stated with tests by affine schemes $\operatorname{Spec} R' \to V$ only, and $V$ need not be affine. In the corollary, $A_g$ is any group pullback of $A$; it is not asked to be an abelian scheme. Result 1 is proved in the same file: [IsProjByOfOpenImmersion.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/IsProjByOfOpenImmersion.lean#L27). The second name of the corollary is a wrapper that tries several forms of one proof term under a raised heartbeat limit, and its file imports Mathlib twice: [ExistsBasicOpenBaseChangeStableSectionBasisStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/DivisorProofs/ExistsBasicOpenBaseChangeStableSectionBasisStatement.lean#L1). We read the statements of results 1 to 6, not their proofs. The explanation of result 3 above is ours.
