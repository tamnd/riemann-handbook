---
title: Volumes of flag subgroups and of orbits
decls:
  - level_s_all_split
  - locMassTyp
  - PI.AprimeInfAsm.aprimeInf_of_hinfCompact
  - PI.AprimeInfAsm.aprime_infinite_real
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Volumes of flag subgroups and of orbits

This section closes three volume computations by supplying their inputs. The first splits the volume of the level subgroup of a flag parabolic over the finite adeles into a product of a unipotent volume and a Levi volume. The second computes the local mass of a type at a split place as a ratio of volumes of compact open subgroups. The third gives the constant $a'$ in the disintegration of the Haar measure of the real unitary group along the orbit of a frame. Each statement is the conclusion of a theorem proved in another chapter, with all its hypotheses discharged here except two at infinity. The results are used in the steps that need [nonempty hypotheses](/step/nonempty-hyps/) and in the theorem that the [archimedean constant holds](/entry/aprime-inf-holds/). For the background see [adelic points and compact open subgroups](/learn/groups/#adelic-points-and-compact-open-subgroups) and [parabolic subgroups](/learn/groups/#parabolic-subgroups).

### The level splitting

Let $E/F$ be a CM extension with involution $\sigma$, and let $J$ be a nondegenerate Hermitian $M \times M$ matrix over $E$. Let $U_J$ be its unitary group. We use the notation of the section on the [level splitting of the flag parabolic](/entry/level-splitting-of-heisenberg-levi/). For a standard frame $P$ of rank $r$ and norm $T$ there are flag subgroups $S$, $N$ and $H$ of $U_J(\mathbb{A}_f)$, with $S = N \rtimes H$. For a set $\Lambda \subseteq E^M$, $K(\Lambda)$ is the subgroup of $g \in U_J(\mathbb{A}_f)$ with $g_v \Lambda_v = \Lambda_v$ at every finite place, and $K_S(\Lambda) = S \cap K(\Lambda)$, $K_N(\Lambda) = N \cap K(\Lambda)$, $K_H(\Lambda) = H \cap K(\Lambda)$. Three sets $\Lambda_X, \Lambda_W, \Lambda_Y$ are adapted to $P$ if $\Lambda_X$ lies in the span of the $e_a$, $\Lambda_Y$ in the span of the $f_a$, and each vector of $\Lambda_W$ is orthogonal to all $e_a$ and $f_a$.

**Theorem 4.6.1 (Level splitting for all CM extensions).** Let $E/F$ be a CM extension of number fields and $J$ a nondegenerate Hermitian matrix. Let $P$ be a standard frame, let $\Lambda_X, \Lambda_W, \Lambda_Y$ be adapted to $P$, and put $\Lambda = \Lambda_X \cup \Lambda_W \cup \Lambda_Y$. Let $\mu_N$ and $\mu_H$ be Haar measures on $N$ and $H$. Then there is a Haar measure $\mu_S$ on $S$ with
$$\int_S f \, d\mu_S = \int_N \int_H f(n h) \, d\mu_H(h) \, d\mu_N(n)$$
for every measurable $f \geq 0$, and every such $\mu_S$ satisfies
$$\mu_S(K_S(\Lambda)) = \mu_N(K_N(\Lambda)) \, \mu_H(K_H(\Lambda)).$$

Lean: `level_s_all_split`.

*Proof.* This is [level splitting](/entry/level-splitting-of-heisenberg-levi/) applied to its two inputs. The first is the Heisenberg structure of $N$ for all CM extensions, which is proved in the same section. The second is the Levi hypothesis for every CM extension, every $J$ and every standard frame: there are a closed subgroup $A \subseteq N$ and a continuous map $\ell$ with $\ell(n) \in A$ and $\ell(n)^{-1} n \in N_0$ for $n \in N$, $A \cap N_0 = \{1\}$, $N$ normalizes $N_0$, and $H$ commutes with $A$. It is supplied by a proved lemma on the Levi part. $\square$

**Remark 4.6.2.** The sets $\Lambda_X$, $\Lambda_W$ and $\Lambda_Y$ are arbitrary subsets of $E^M$, not lattices. For example, all three may be empty. Then $\Lambda_v = 0$ at every place, $K(\Lambda)$ is all of $U_J(\mathbb{A}_f)$, and the formula says $\mu_S(S) = \mu_N(N) \mu_H(H)$, which holds in $[0, \infty]$.

### The local mass of a type

We use the setting of the section on [the local mass of a type at a split place](/entry/local-mass-type-of-parts/). So $v$ is a finite place of $F$ that splits in $E$ and is unramified, $g$ is the prime below $v$ with absolute norm of $v$ equal to $g$, $\Lambda_v$ is self-dual, $K_v$ is its stabilizer and $K_{g,v}$ is the principal congruence subgroup of level $g$. Frames $P$ have attached groups $S^0_P \subseteq S_P$, a unipotent parametrization $\mathcal{U}$, orbit measures $\omega_T$, the set $\Omega_g$ of pairs of tuples that are congruent modulo $g$ after rescaling, and the volume $\operatorname{vol}(\mathcal{U}_g)$.

**Theorem 4.6.3 (Local mass of a type).** Let $P$ and $P'$ be frames with values $T$ and $T'$, with $\ell P$ and $\ell P'$ primitive for $\Lambda_v$, and assume that there is $\kappa \in K_v$ with $\kappa \cdot \ell P' - \ell P \in g \Lambda_v^{r+1}$. Let $\mu_G$ be a Haar measure on $U(F_v)$, and $\mu_S$, $\mu_{S'}$ Haar measures on $S_P$, $S_{P'}$ tied to $\mu_G$. Then
$$\frac{(\omega_{T} \times \omega_{T'})(\Omega_g)}{\operatorname{vol}(\mathcal{U}_g)} = \frac{\mu_G(K_v) \, \mu_G(K^\natural_v)}{\mu_S(S_P \cap K_v) \, \mu_{S'}(S_{P'} \cap K_v)},$$
where $K^\natural_v$ is the set of products $s \kappa$ with $s \in S_P \cap K_v$ and $\kappa \in K_{g,v}$.

Lean: `locMassTyp`.

*Proof.* This is the theorem on the [local mass of a type](/entry/local-mass-type-of-parts/) applied to its two inputs. The first is right invariance: every Haar measure $\mu_G$ on $U(F_v)$ satisfies $\mu_G(A \kappa) = \mu_G(A)$ for measurable $A$ and $\kappa \in K_v$. It is a proved lemma. The second is the existence of integral unipotents: for every integral point $u$ of $\mathcal{U}$ there is $s \in K_v$ that acts on the vectors of $P$ by the unipotent matrix of $u$. It is derived from a proved lemma on the reduction at a split place. $\square$

### The archimedean orbit constant

Let $E/F$ be a CM extension and $J$ a Hermitian matrix of size $n$, and let $G_\infty$ be the unitary group of $J$ over $F \otimes_{\mathbb{Q}} \mathbb{R}$. Let $d$ be the number of infinite places of $F$, and let $k$ be the integer of the setting. For a word $u$ let $H_\infty(u) \subseteq G_\infty$ be the stabilizer of the frame of $u$, a tuple of $2r + 1$ vectors. For $k \geq 1$ put
$$V_k = \prod_{i=1}^{k} \frac{(2\pi)^i}{(i-1)!}.$$

**Definition 4.6.4 (Compact stabilizers at infinity).** The *compactness of the stabilizers at infinity* is the statement that for every setting and every word $u$ the group $H_\infty(u)$ is compact.

**Definition 4.6.5 (Gauge volumes of the compact unitary groups).** The *gauge volume statement* says: for every $k$, the compact group $U(k)$ has a gauge density, that is the ratio $\mu(\exp B_\rho)/\operatorname{vol}(B_\rho)$ of the Haar measure of the image of a small ball in the Lie algebra to the volume of the ball has a positive limit $g$ as $\rho \to 0^+$, and the measure $\mu / g$ gives $U(k)$ the total mass $V_k$.

**Theorem 4.6.6 (Archimedean orbit constant).** Assume that the stabilizers at infinity are compact and the gauge volume statement. Let $u, u'$ be words and $\psi$ a standard character of $\mathbb{A}_F$ that satisfies the compatibility conditions of the setting, and let the gauge density exist at each infinite place. Let $a' > 0$ be such that self-dual measures on tuples and on Hermitian matrices at infinity exist, and for every such choice and every family of fibre measures over the Gram map,
$$\int_{G_\infty} f \, d\mu_G = a' \int_y \int_{H_\infty(u')} f(s(y) h) \, d\mu_H(h) \, d\mathrm{fib}(y)$$
for all measurable $f \geq 0$ and all sections $s$ of the orbit map. Then
$$a' = \frac{g_U \, V_k^{\,d} \, T_{u'}^{-kd}}{\mu_H\big(H_\infty(u')\big)},$$
where $g_U$ is the product of the gauge constants over the infinite places and $T_{u'}$ is the integer attached to $u'$.

Lean: `PI.AprimeInfAsm.aprimeInf_of_hinfCompact` (also `PI.AprimeInfAsm.aprime_infinite_real`, the same statement).

*Proof.* This is the theorem on the [archimedean orbit constant from the group chart](/entry/aprime-inf-of-grp/) applied to four inputs. The first is the compactness of the stabilizers, which is a hypothesis. The second is the limit of Haar volumes of small tubes around a standard chart of the group; it is derived from the gauge volume statement and a proved lemma on exponentials of products of unitary groups. The third says that the self-dual measure on Hermitian matrices at infinity is Lebesgue measure in suitable orthonormal real coordinates. The fourth is a Jacobian computation at each real place, for the map that sends a pair of Lie algebra and Hermitian coordinates to tuples. The last two are proved lemmas. $\square$

The two hypotheses are proved elsewhere, and the theorem that the [archimedean constant holds](/entry/aprime-inf-holds/) supplies them. The value of $a'$ is then used in the [real bracket](/entry/real-bracket-holds/).

**Remark 4.6.7 (Formalization).** The archimedean theorem has two names with the same statement, and the second only calls the first; see [AprimeInf.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/AprimeInf.lean#L10). The compatibility conditions on $\psi$ and the setting were not unfolded. In the level splitting theorem the nondegeneracy of $J$ is asked twice, once for all CM data and once inside the statement for each frame; see [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/LevelKSplit.lean#L47) and [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/LevelKSplit.lean#L27). The sets $\Lambda_X, \Lambda_W, \Lambda_Y$ are sets of vectors with no lattice condition, and one caller passes empty sets, and so uses only the existence of $\mu_S$; see [ProductDecompositionHolds.lean](lean:Formalism/PeriodIntegrals/UnitaryGroupMassFormula/WeightedMeasureSplitting/ProductDecompositionHolds.lean#L38). The lemmas on the Levi part, right invariance, split reduction, small tubes, measures at infinity and the real Jacobians were not unfolded beyond their statements. The other two theorems are in [LevelKSplit.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LevelKSplit.lean#L7) and [LocMassTyp.lean](lean:Formalism/PeriodIntegrals/OrbitalBoundsConclusion/LocMassTyp.lean#L7).
