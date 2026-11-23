---
title: The minimal parabolic modulo rational points
decls:
  - GlobalTheory.T.minimal_parabolic_rational_compact
  - GlobalTheory.CompanionTheory.ParCocompact.minParOne_cocompact
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The minimal parabolic modulo rational points

A Siegel set has three factors. The torus factor is a cone, and the compact factor was built in the [previous section](/entry/exists-compact-iwasawa-good/). This section builds the first factor. It proves that the group $P^1$ of the minimal parabolic is compact modulo its rational points: there is a compact $\Omega \subseteq P^1$ with $P^1 = P(F)\,\Omega$. This is the unitary case of the classical fact that $P(F) \backslash P(\mathbb{A})^1$ is compact for a minimal parabolic $P$ ([arithmetic subgroups and Siegel sets](/learn/trace-formula/#arithmetic-subgroups-and-siegel-sets)). It is used twice in the [construction of Siegel domains](/entry/cov-main/). We keep the notation of the previous section: $E/F$ is a CM extension, $J$ a nondegenerate Hermitian matrix, $(X, Y)$ a Witt frame of rank $r$, and $P$, $P^1$, $M$, $N$ the minimal parabolic, its norm-one part, its Levi subgroup and its unipotent radical.

**Definition 3.2.1 (Height of a rational vector).** For $\xi \in \mathbb{A}_E^n$ write its coordinates in a fixed basis of $E$ over $F$, so that $\xi$ becomes a vector $y$ of adeles of $F$. The adelic norm of $\xi$ is
$$\|\xi\|_{\mathbb{A}} = \prod_{w \mid \infty} \|y_w\|_2^{m_w} \cdot \prod_{v < \infty} \|y_v\|_v,$$
where $\|\cdot\|_2$ is the Euclidean norm, $m_w \in \{1, 2\}$ is the multiplicity of the infinite place $w$, and $\|y_v\|_v$ is the maximum of the $v$-adic absolute values of the coordinates. For $g \in G(\mathbb{A})$ and $\xi \in E^n$ the height of $\xi$ at $g$ is
$$\operatorname{ht}_g(\xi) = \|g^{-1} \xi\|_{\mathbb{A}}.$$

By the product formula, $\operatorname{ht}_g(c\xi) = \operatorname{ht}_g(\xi)$ for $c \in F^\times$, and $\operatorname{ht}_{\gamma g}(\gamma \xi) = \operatorname{ht}_g(\xi)$ for $\gamma \in G(F)$. The height is the function that measures how far $g$ is from a compact set modulo $G(F)$: by Mahler's compactness criterion, a set of $g$ is compact modulo rational points when the heights of all nonzero rational vectors are bounded below on it.

We use three inputs. The first two are forms of this criterion, and the third is the Levi decomposition of $P^1$.

**Theorem 3.2.2 (Compact quotients of commutants).** Let $(S_k)_{k \in I}$ be a finite family of matrices in $M_n(E)$ and let $L \subseteq G(\mathbb{A})$ be a closed subgroup such that:

1. every $g \in L$ commutes with every $S_k$;
2. every $\gamma \in G(F)$ that commutes with every $S_k$ lies in $L$;
3. there is $\varepsilon > 0$ with $\operatorname{ht}_g(\xi) \ge \varepsilon$ for all $g \in L$ and all nonzero $\xi \in E^n$.

Then there is a compact $\Omega \subseteq L$ such that every $g \in L$ is $\delta \omega$ with $\delta \in L \cap G(F)$ and $\omega \in \Omega$.

**Theorem 3.2.3 (Height bound from anisotropic forms).** Let $(H_j)_{j \in I}$ be a finite family of Hermitian matrices that is jointly anisotropic: if $\xi \in E^n$ and $\xi^* H_j \xi = 0$ for all $j$, then $\xi = 0$. Let $L \subseteq G(\mathbb{A})$ be a set such that for every $g \in L$ and every $j$ there is an idele $s$ of $F$ with module $|s| \ge 1$ and
$$(g^{-1}\xi)^* H_j (g^{-1}\xi) = s \cdot \xi^* H_j \xi \quad \text{for all } \xi \in E^n.$$
Then there is $\varepsilon > 0$ with $\operatorname{ht}_g(\xi) \ge \varepsilon$ for all $g \in L$ and all nonzero $\xi \in E^n$.

**Theorem 3.2.4 (Levi decomposition of $P^1$).** Every $p \in P^1$ can be written $p = um$ with $u \in N$ and $m \in M \cap P^1$.

The three results are taken as given. Together with the next lemma they give the main result.

**Lemma 3.2.5 (The unipotent radical).** There is a compact $C$ such that every $u \in N$ can be written $u = \delta c$ with $\delta \in N \cap G(F)$ and $c \in N \cap C$.

Lean: `GlobalTheory.CompanionTheory.UnipCocompact.unipMin_cocompact`.

*Proof.* This is the compactness of $N(F) \backslash N(\mathbb{A})$. For $u \in N$ the matrix $u - 1$ lies in a space of nilpotent matrices that is filtered by weights attached to the columns of $X$, and the product of two such matrices has larger weight. The space is defined over $E$, and $\mathbb{A}_E / E$ is compact. So one can move $u$ by a rational element of $N$ into a fixed compact set one weight at a time, starting with the smallest weight. $\square$

**Theorem 3.2.6 (The norm-one parabolic is compact modulo rational points).** Let $E/F$ be a CM extension, $J$ Hermitian and nondegenerate, and $(X, Y)$ a Witt frame of rank $r$. Then there is a compact set $\Omega \subseteq P^1$ such that every $p \in P^1$ can be written
$$p = \delta \omega, \qquad \delta \in G(F) \cap P, \quad \omega \in \Omega.$$

Lean: `GlobalTheory.CompanionTheory.ParCocompact.minParOne_cocompact` (also `GlobalTheory.T.minimal_parabolic_rational_compact`, a second name).

*Proof.* First the Levi part. For each $i$ let $\pi_i$ be the rank-one map $z \mapsto x_i \cdot (y_i^* J z)$ and $\pi'_i$ the map $z \mapsto y_i \cdot (x_i^* J z)$. These are the projections onto the lines $E x_i$ and $E y_i$ along the other summands of $E^n = \langle X \rangle \oplus \langle Y \rangle \oplus V_0$. An element of $G(\mathbb{A})$ lies in $M$ exactly when it commutes with all of them. Let $L = M \cap P^1$. It is a closed subgroup, it commutes with the family $(\pi_i, \pi'_i)$, and a rational element that commutes with this family is in $M$; it is also in $P^1$ by the product formula, since its diagonal entries are in $E^\times$. So conditions 1 and 2 of the theorem on commutants hold.

For condition 3 we use the family of Hermitian forms
$$|y_i^* J \xi|^2, \qquad |x_i^* J \xi|^2 \quad (1 \le i \le r), \qquad h(\pi_0 \xi, \pi_0 \xi),$$
where $\pi_0 = 1 - \sum_i (\pi_i + \pi'_i)$ is the projection onto $V_0$. If all of them vanish at $\xi$, then the coordinates of $\xi$ along $X$ and $Y$ are $0$, and $\pi_0\xi$ is an isotropic vector of $V_0$, so it is $0$ because $V_0$ is anisotropic. Thus the family is jointly anisotropic. An element $m \in L$ multiplies $x_i$ by an idele $d_i$ of $E$ with $|d_i| = 1$ and acts on $V_0$ by a unitary map. So each form of the family is multiplied by the norm of an idele of module $1$ when $\xi$ is replaced by $m^{-1}\xi$. The height bound applies and gives $\varepsilon$. The theorem on commutants now gives a compact $C' \subseteq M \cap P^1$ with $M \cap P^1 = (M \cap G(F)) C'$.

Now the whole group. Let $C$ be as in the lemma on the unipotent radical, and put $\Omega = (C \cap P^1)\, C'$. This set is compact, since $P^1$ is closed. It lies in $P^1$, since $P^1$ is closed under products. Let $p \in P^1$. Write $p = um$ with $u \in N$ and $m \in M \cap P^1$. Write $m = \delta c'$ with $\delta \in M \cap G(F)$ and $c' \in C'$. The Levi subgroup normalizes $N$, so $\delta^{-1} u \delta \in N$; write it as $\delta' c$ with $\delta' \in N \cap G(F)$ and $c \in N \cap C$. Then
$$p = u \delta c' = \delta (\delta^{-1} u \delta) c' = (\delta \delta')(c c').$$
Here $\delta\delta'$ is rational and lies in $P$, and $cc' \in \Omega$, because $N \subseteq P^1$. $\square$

**Remark 3.2.7.** The compact set $\Omega$ meets every rational coset of $P^1$. In the classical language, $P(F) \backslash P(\mathbb{A})^1$ is compact; see A. Borel, *Introduction aux groupes arithmétiques*, and Moeglin and Waldspurger, *Spectral Decomposition and Eisenstein Series*, Chapter I. Here the statement is proved only for the minimal parabolic of a unitary group over a CM field.

**Remark 3.2.8 (Formalization).** The three theorems before the lemma are statements of the form `GlobalTheory.T.*` (`commutant_closed_subgroup_compact_quotient`, `idele_bound_of_joint_anisotropic`, `minimal_parabolic_levi_decomposition`), used here as inputs. The weight filtration in the proof of the lemma is only sketched above. The proof of the theorem is in [MinimalParabolicRationalCompact.lean](lean:Development/AutomorphicSpectrum/Proofs/BlockDecomposition/MinimalParabolicRationalCompact.lean#L36).
