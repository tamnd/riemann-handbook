---
title: Counting isotropic vectors
decls:
  - GlobalTheory.T.hyperbolic_fundamental_domain_cover
  - GlobalTheory.CompanionTheory.SW.IsoMain.integral_isotropic_lines_le_flow_sum
  - GlobalTheory.T.hyperbolic_finite_volume_integral_bound
  - GlobalTheory.CompanionTheory.SW.IsoCount.mean_isotropic_count_le
  - GlobalTheory.T.isotropic_vector_count_box_bound
  - GlobalTheory.CompanionTheory.SW.mean_isotropic_box
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Counting isotropic vectors

Let $U_J$ be the unitary group of a nondegenerate Hermitian matrix $J$ over a CM extension, as in the section on finite volume. This section bounds the average, over the automorphic quotient $U_J(F) \backslash U_J(\mathbb{A}_F)$, of the number of nonzero isotropic rational vectors in an adelic box of radius $r$, by a constant times $r^{2[F:\mathbb{Q}](M-1)}$. The method is the classical one of reduction theory. A nonzero isotropic vector spans a line with a hyperbolic partner, the stabilizer of the line is a maximal parabolic subgroup $P$, the sum over isotropic vectors unfolds to an integral over $P \cap U_J(F) \backslash U_J(\mathbb{A}_F)$, and that integral is bounded on a Siegel set by a sum over the levels of a real flow. The result is used in the next section for the theta measure of a box, which serves the step [EveryCharacter](/step/every-character/).

### Counting integrals and boxes

We keep the notation of the section on finite volume: $(F, E, \sigma)$ is a CM extension, $\mathbb{A}_E = \mathbb{A}_F \otimes_F E$, $J \in M_M(E)$ is nondegenerate Hermitian with form $h(x, y) = \sigma(x)^{\mathsf T} J y$, and $h$ also denotes its extension to $\mathbb{A}_E^M$. A vector $X \in E^M$ is *isotropic* if $h(X, X) = 0$. Write $Z_J$ for the set of nonzero isotropic vectors in $E^M$. The group $U_J(\mathbb{A}_F)$ acts on $\mathbb{A}_E^M$ by matrix multiplication, and $E^M$ embeds in $\mathbb{A}_E^M$.

**Definition 1.9.1 (Counting integral).** Let $\mu$ be a Haar measure on $U_J(\mathbb{A}_F)$ and $\mathcal{F}$ a fundamental domain for $U_J(F)$. For a set $S \subseteq E^M$ and a function $\Phi \colon \mathbb{A}_E^M \to [0, \infty]$, put
$$I_J(S, \Phi) = \int_{\mathcal{F}} \sum_{X \in S} \Phi(h^{-1} X)\, d\mu(h).$$

Lean: `GlobalTheory.CompanionTheory.SW.cntI`.

In the code the vectors are tuples of $n$ vectors; this section uses only $n = 1$.

**Definition 1.9.2 (Adelic box).** Fix a basis $b$ of $E$ over $F$, an integer $N \geq 1$ and $r \in \mathbb{R}$. The *box* $B(N, r) \subseteq \mathbb{A}_E^M$ is the set of $Y$ such that, at each finite place $v$ of $F$, the $b$-coordinates of the entries of $N Y_v$ lie in $\mathcal{O}_{F_v}$, and such that the sum of the absolute values of the $b$-coordinates of the entries of $Y_\infty$, over all entries and all infinite places, is at most $r$.

Lean: `GlobalTheory.CompanionTheory.SW.box`.

**Definition 1.9.3 (Hyperbolic extension).** For $J \in M_M(E)$ let $J^{+}$ be the $(M + 2) \times (M + 2)$ matrix
$$J^{+} = \begin{pmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & J \end{pmatrix}.$$

Lean: `GlobalTheory.CompanionTheory.SW.hypJ`.

So $E^{M+2}$ with the form of $J^{+}$ is the orthogonal sum of a hyperbolic plane and $E^M$. Let $e_0 = (1, 0, \ldots, 0)$ and $e_1 = (0, 1, 0, \ldots, 0)$. Then $e_0$ and $e_1$ are isotropic and $h^{+}(e_1, e_0) = 1$.

**Definition 1.9.4 (Real flow).** A *real flow* is a continuous homomorphism $\tau \colon \mathbb{R} \to \mathbb{A}_E^\times$, from the additive group of $\mathbb{R}$, for which there is a continuous ring homomorphism $\theta \colon \mathbb{R} \to \mathbb{A}_{F,\infty}$ such that $\tau(x)$ has infinite component $\theta(e^x) \otimes 1$ and finite component $1$.

Lean: `GlobalTheory.CompanionTheory.SW.IsFlow`.

An example is $\theta(s) = (s, \ldots, s)$. Then $\tau(x)$ multiplies each infinite coordinate by $e^x$, so $\tau(x) B(N, r) = B(N, e^x r)$. In general the flow acts on $\mathbb{A}_E^M$ by scalars, so it commutes with the action of $U_J(\mathbb{A}_F)$.

### Unfolding along an isotropic line

**Theorem 1.9.5 (Isotropic lines and the flow).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 0$, $J \in M_M(E)$ nondegenerate Hermitian such that $U_J$ has finite volume, and $\tau$ a real flow. Let $\mu$ be a Haar measure on $U_{J^+}(\mathbb{A}_F)$ and $\mathcal{F}$ a fundamental domain for $U_{J^+}(F)$. Then there are a compact set $Y \subseteq \mathbb{A}_E^{M+2} \times \mathbb{A}_E^{M+2}$ and $K < \infty$ with $h^{+}(y_2, y_1) = 1$ for all $(y_1, y_2) \in Y$, such that the following holds. Let $\Phi \colon \mathbb{A}_E^{M+2} \to [0, \infty]$ be measurable with $\Phi(l y) = \Phi(y)$ for all $l \in E^\times$, let $g \colon \mathbb{Z} \to [0, \infty]$ satisfy $\Phi(\tau(-j) y_1) \leq g(j)$ for all $j$ and all $(y_1, y_2) \in Y$, and let $L \subseteq Z_{J^+}$ contain no two distinct proportional vectors. Then
$$I_{J^+}(L, \Phi) \leq K \sum_{j \in \mathbb{Z}} g(j)\, e^{-2[F:\mathbb{Q}](M+1) j}.$$

Lean: `GlobalTheory.T.hyperbolic_fundamental_domain_cover` (also `GlobalTheory.CompanionTheory.SW.IsoMain.integral_isotropic_lines_le_flow_sum`).

*Proof.* Write $G = U_{J^+}(\mathbb{A}_F)$, $\Gamma = U_{J^+}(F)$, and let $P \subseteq G$ be the stabilizer of the line $\mathbb{A}_E^\times e_0$. We use five facts, proved in another part of the development.

1. *Siegel sets.* There are an s-finite measure $\nu$ on $G$, invariant under left translation by $P$ and positive on each neighbourhood of $1$, measurable sets $S_j \subseteq P$ for $j \in \mathbb{Z}$, a compact set $\omega \subseteq \mathbb{A}_E^\times$ and $K_0 < \infty$, such that $\nu(S_j) \leq K_0 e^{-2[F:\mathbb{Q}](M+1) j}$, such that each $p \in S_j$ satisfies $p e_0 = \tau(j) c\, e_0$ for some $c \in \omega$, and such that for $\nu$-almost every $p$ there are $\gamma \in P \cap \Gamma$ and $j$ with $\gamma p \in S_j$. The statement of this fact assumes that $U_J$ has finite volume.
2. *Cocompactness.* There is a compact $C \subseteq G$ with $G = P C$.
3. *Comparison.* For $P$, $\nu$ and $C$ as above there are a compact $C' \subseteq G$ and $K_1 < \infty$ such that, for every countable subgroup $\Gamma' \subseteq P$ with fundamental domain $\mathcal{F}'$, every measurable $S$ such that $\nu$-almost every $p$ has a translate $\gamma p \in S$ with $\gamma \in \Gamma'$, and all measurable $f, g'$ with $f$ left invariant under $\Gamma'$, $f = 0$ outside $P C$ and $f(p c) \leq g'(p)$ for $p \in S$, $c \in C'$, we have $\int_{\mathcal{F}'} f\, d\mu \leq K_1 \int_S g'\, d\nu$.
4. *Witt's theorem.* $U_{J^+}(E)$ acts transitively on $Z_{J^+}$.
5. *Unfolding.* For a subgroup $\Gamma' \subseteq \Gamma$ and a set of representatives $r_q$ of $\Gamma' \backslash \Gamma$, there is a fundamental domain $\mathcal{F}'$ for $\Gamma'$ with $\int_{\mathcal{F}} \sum_q f(r_q h)\, d\mu(h) = \int_{\mathcal{F}'} f\, d\mu$ for measurable $f \geq 0$.

Let $Y$ be the image of $\omega \times C'$ under $(a, c) \mapsto (a^{-1} c^{-1} e_0,\ \sigma(a) c^{-1} e_1)$, and $K = K_1 K_0$. The set $Y$ is compact. Since $c^{-1}$ preserves $h^{+}$, we get $h^{+}(\sigma(a) c^{-1} e_1, a^{-1} c^{-1} e_0) = a\, a^{-1} h^{+}(e_1, e_0) = 1$.

Let $\Phi$, $g$ and $L$ be as in the statement. By Witt's theorem, for each $X \in L$ there is $\gamma_X \in \Gamma$ with $\gamma_X^{-1} e_0 = X$. An element of $P \cap \Gamma$ maps $e_0$ to $l e_0$ with $l \in E^\times$. So if $\gamma_X$ and $\gamma_{X'}$ lie in the same coset of $P \cap \Gamma$, then $X'$ is a multiple of $X$, and $X' = X$ by the hypothesis on $L$. Put $f(h) = \Phi(h^{-1} e_0)$. It is measurable, and left invariant under $P \cap \Gamma$ because $\Phi$ is invariant under $E^\times$. Since $X \mapsto (P \cap \Gamma)\gamma_X$ is injective, fact 5 gives
$$I_{J^+}(L, \Phi) = \int_{\mathcal{F}} \sum_{X \in L} f(\gamma_X h)\, d\mu(h) \leq \int_{\mathcal{F}'} f\, d\mu,$$
with $\mathcal{F}'$ a fundamental domain for $P \cap \Gamma$.

Apply fact 3 with $\Gamma' = P \cap \Gamma$, $S = \bigcup_j S_j$ and $g' = \sum_j g(j) \mathbf{1}_{S_j}$. By fact 2 every $x \in G$ is $p c$ with $p \in P$ and $c \in C$. If $p \in S_j$ with $p e_0 = \tau(j) a\, e_0$, $a \in \omega$, and $c \in C'$, then $(p c)^{-1} e_0 = \tau(-j) a^{-1} c^{-1} e_0$, since the scalars commute with $c^{-1}$. So $f(p c) = \Phi(\tau(-j) y_1)$ with $(y_1, y_2) \in Y$, and $f(p c) \leq g(j) \leq g'(p)$. Fact 3 gives
$$\int_{\mathcal{F}'} f\, d\mu \leq K_1 \sum_j g(j)\, \nu(S_j) \leq K_1 K_0 \sum_j g(j)\, e^{-2[F:\mathbb{Q}](M+1) j}. \qquad \square$$

### The count under the flow

**Theorem 1.9.6 (Isotropic count under the flow).** Let $(F, E, \sigma)$, $J$, $\tau$, $\mu$ and $\mathcal{F}$ be as in the last theorem, and assume $M \geq 1$. Let $\Omega \subseteq \mathbb{A}_E^{M+2}$ be compact. Then there is $C$ such that for all $r > 0$
$$I_{J^+}\bigl(Z_{J^+},\ \mathbf{1}_\Omega(\tau(-\log r)\, \cdot\,)\bigr) \leq C\, r^{2[F:\mathbb{Q}](M+1)}.$$

Lean: `GlobalTheory.T.hyperbolic_finite_volume_integral_bound` (also `GlobalTheory.CompanionTheory.SW.IsoCount.mean_isotropic_count_le`).

*Proof.* We use two more facts, proved in another part of the development. The first is a count of rational points under the flow: for $m \geq 0$ and a compact $\Omega' \subseteq \mathbb{A}_E^m$ there are $x_0$ and $C_0$ such that
$$\sum_{X \in E^m \setminus 0} \mathbf{1}_{\Omega'}(\tau(-x) X) \leq \begin{cases} 0, & x < x_0, \\ C_0\, e^{2[F:\mathbb{Q}] m x}, & x \geq x_0. \end{cases}$$
The second is a bound for a geometric series: for $D \geq 1$, $M \geq 1$, $x_0$ and $C_0$ there is $C'$ with
$$\sum_{j \in \mathbb{Z},\ j + \log r \geq x_0} C_0\, e^{2D(j + \log r)}\, e^{-2D(M+1) j} \leq C' r^{2D(M+1)} \quad (r > 0).$$
The series converges because $M \geq 1$.

Let $Y$ and $K$ come from the last theorem. Let $\Omega' \subseteq \mathbb{A}_E$ be the image of $Y \times \Omega$ under $((y_1, y_2), y) \mapsto h^{+}(y_2, y)$. It is compact. Take $x_0$ and $C_0$ for $\Omega'$ and $m = 1$, and $C'$ for $D = [F:\mathbb{Q}]$.

Fix $r > 0$ and put $t = \tau(-\log r)$. Choose a set $L \subseteq Z_{J^+}$ with one vector on each line, and put $\Phi(y) = \sum_{l \in E^\times} \mathbf{1}_\Omega(t\, l\, y)$. Then $\Phi$ is measurable and invariant under $E^\times$, and each $X \in Z_{J^+}$ is $l X_0$ for one pair $(X_0, l) \in L \times E^\times$, so
$$I_{J^+}\bigl(Z_{J^+}, \mathbf{1}_\Omega(t\, \cdot\,)\bigr) \leq I_{J^+}(L, \Phi).$$
Let $g(j) = 0$ if $j + \log r < x_0$ and $g(j) = C_0 e^{2[F:\mathbb{Q}](j + \log r)}$ otherwise. Let $(y_1, y_2) \in Y$ and $j \in \mathbb{Z}$. If $t\, l\, \tau(-j) y_1 \in \Omega$, then $h^{+}(y_2, t\, l\, \tau(-j) y_1) = \tau(-(j + \log r))\, l$ lies in $\Omega'$, because $h^{+}(y_2, y_1) = 1$. So $\Phi(\tau(-j) y_1)$ is at most the number of $l \in E^\times$ with $\tau(-(j + \log r)) l \in \Omega'$, which is at most $g(j)$ by the count under the flow. The last theorem and the geometric series give
$$I_{J^+}(L, \Phi) \leq K \sum_j g(j)\, e^{-2[F:\mathbb{Q}](M+1) j} \leq K C' r^{2[F:\mathbb{Q}](M+1)}. \qquad \square$$

### Isotropic vectors in a box

**Theorem 1.9.7 (Isotropic vectors in a box).** Let $(F, E, \sigma)$ be a CM extension, $M \geq 3$, $J \in M_M(E)$ nondegenerate Hermitian, $\mu$ a Haar measure on $U_J(\mathbb{A}_F)$, $\mathcal{F}$ a fundamental domain for $U_J(F)$, $b$ a basis of $E$ over $F$, and $N \geq 1$. Then there is $C$ such that for all $r > 0$
$$I_J\bigl(Z_J,\ \mathbf{1}_{B(N, r)}\bigr) \leq C\, r^{2[F:\mathbb{Q}](M-1)}.$$

Lean: `GlobalTheory.T.isotropic_vector_count_box_bound` (also `GlobalTheory.CompanionTheory.SW.mean_isotropic_box`).

*Proof.* If $Z_J$ is empty, the left side is $0$ and $C = 0$ works. Otherwise we use four facts, proved in another part of the development.

1. *Splitting a hyperbolic plane.* If $x \in Z_J$, then $M = M_1 + 2$ and there are $g \in \mathrm{GL}_M(E)$ and a nondegenerate Hermitian $J_1 \in M_{M_1}(E)$ with $J_1^{+} = \sigma(g)^{\mathsf T} J g$.
2. *Transport.* If $J' = \sigma(g)^{\mathsf T} J g$ with $g \in \mathrm{GL}_M(E)$, there are a Haar measure $\mu'$ on $U_{J'}(\mathbb{A}_F)$ and a fundamental domain $\mathcal{F}'$ with $\mu'(\mathcal{F}') = \mu(\mathcal{F})$ and $I_J(S, \Phi) = I_{J'}(g^{-1} S, \Phi(g\, \cdot\,))$ for all $S$ and $\Phi$.
3. A real flow $\tau$ exists.
4. *Boxes.* Each $B(N, r)$ is compact, and $\tau(x) Y \in B(N, e^x r)$ if and only if $Y \in B(N, r)$.

Take $M_1$, $g$ and $J_1$ from fact 1, and $\mu'$, $\mathcal{F}'$ for $J' = J_1^{+}$ from fact 2. A vector $X$ lies in $Z_{J'}$ if and only if $g X \in Z_J$, so $g^{-1} Z_J = Z_{J'}$. By fact 4 with $x = -\log r$, $g Y \in B(N, r)$ if and only if $\tau(-\log r) Y \in g^{-1} B(N, 1)$, since $g$ commutes with scalars. So
$$I_J\bigl(Z_J, \mathbf{1}_{B(N, r)}\bigr) = I_{J'}\bigl(Z_{J'},\ \mathbf{1}_{\Omega}(\tau(-\log r)\, \cdot\,)\bigr), \qquad \Omega = g^{-1} B(N, 1),$$
and $\Omega$ is compact. Now $M_1 = M - 2 \geq 1$, and $U_{J_1}$ has finite volume by the [theorem on finite volume](/entry/fin-vol-unitary-group/). The theorem on the isotropic count under the flow, applied to $J_1$, $\tau$, $\mu'$, $\mathcal{F}'$ and $\Omega$, gives the bound $C r^{2[F:\mathbb{Q}](M_1 + 1)} = C r^{2[F:\mathbb{Q}](M-1)}$. $\square$

**Remark 1.9.8 (Classical form).** The method of Siegel sets and the unfolding of a sum over a $\Gamma$-orbit to a sum over $(P \cap \Gamma) \backslash \Gamma$ are the reduction theory of arithmetic groups (A. Borel, *Introduction aux groupes arithmétiques*, Hermann, 1969). Here the bound on Siegel sets, fact 1 of the first proof, is taken as an input; its statement assumes the finite volume of $U_J$, and $U_J$ is the group of the orthogonal complement of the hyperbolic plane.

**Remark 1.9.9 (Formalization).** The theorem on isotropic lines, in [HyperbolicFundamentalDomainCover.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/HyperbolicFundamentalDomainCover.lean#L27), has no hypothesis $M \geq 1$, and it takes the finite volume of $U_J$ as a hypothesis, although the [theorem on finite volume](/entry/fin-vol-unitary-group/) gives it for every $J$. The facts of the first proof are `GlobalTheory.T.hyperbolic_parabolic_siegel_set_bound`, `GlobalTheory.T.hyperbolic_unitary_stabilizer_cocompact`, `GlobalTheory.CompanionTheory.Adelic.integral_fundamentalDomain_le_siegel`, `GlobalTheory.T.unitary_transitive_on_isotropic_vectors` and `GlobalTheory.CompanionTheory.Adelic.unfold_coset_sum_fundamentalDomain`. The facts of the second proof are `GlobalTheory.T.flow_lattice_count_bounded` and `GlobalTheory.CompanionTheory.Adelic.geom_sum_int`; those of the third are `GlobalTheory.T.isotropic_vector_splits_hyperbolic_plane`, `GlobalTheory.T.fundamental_domain_transport_congruent_form`, `GlobalTheory.T.exists_real_flow_adelic_units` and `GlobalTheory.T.adelic_boxes_compact_exhaust`. We have opened their statements, not their proofs. In [CountingRationalVectorsBoxBound.lean](lean:CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/CountingRationalVectorsBoxBound.lean#L115) the hypothesis $M \geq 3$ is used only to get $M_1 \geq 1$. The basis $b$ is indexed by any $d$, but a basis of $E$ over $F$ has $d = 2$. The three `GlobalTheory.T` names restate the three proved theorems without change.
