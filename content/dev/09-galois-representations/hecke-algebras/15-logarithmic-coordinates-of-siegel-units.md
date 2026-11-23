---
title: Logarithmic coordinates of Siegel units
decls:
  - GlobalTheory.T.siegel_logCoords_alt
  - GlobalTheory.SiegLog.siegel_logCoords
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Logarithmic coordinates of Siegel units

The local theorems of the last three sections are stated for units of the ring $\mathcal{O}_L$ with logarithmic coordinates. This section shows that a smoothed Siegel unit gives such a unit, and it computes the coordinates modulo $p^L$: both are multiples of the value of the smoothed Eisenstein series $F_c(A_1, a_2)$ of weight $1$. This is the lemma on Siegel coordinates in the proof of [the edge class of two Siegel units](/entry/pair-edge-dlog/). There the determinant $\alpha\beta' - \beta\alpha'$ of the coordinates of two units becomes $(A_1h - gB_1)$ times a product of two Eisenstein series.

We keep the notation of [Section 6.12.7](/entry/pair-edge-dlog/): a tower of modular functions $(K_X, \exp, |, s, \mathrm{an}, j_K)$ over $(\Omega_0, \varepsilon)$, the roots of unity $\zeta_{p^m}$ and $\zeta_M$, the subfield $K_X(M)$, the smoothed Siegel units $u_c(A_1, a_2)$, and the sequences $E(A_1, a_2)$ and $F_c(A_1, a_2)$. We also keep the local notation: an odd prime $p$, a closure $\Omega_l$ of $\mathcal{O}$ with a tower $(\zeta_m, q_m)$, integral elements, reparametrizations, embeddings of $\mathcal{O}_L$, logarithmic coordinates and evaluations. For $f \in K_X$ and $r \in \mathbb{Q}$ we write $f_r$ for the coefficient of $q^r$ in the expansion $\exp(f)$.

### Passage from modular functions to the local field

Two maps connect the global field $\Omega_0$ and the field $K_X(p^L)$ with the local field $\Omega_l$.

**Definition 6.15.1 (Cusp embedding).** Let $A$ be a valuation ring of $\Omega_0$. A *cusp embedding* for $A$ is a ring map $j : \Omega_0 \to \Omega_l$ such that:

1. $y \in A$ if and only if $j(y)$ is integral;
2. $j(y)$ is algebraic over $\mathbb{Z}_p$ for every $y$;
3. $j(\zeta_{p^m}) = \zeta_m$ for every $m$;
4. for each $k$ and each integral $e \in \Omega_l$ algebraic over $\mathbb{Z}_p$ there is $a \in A$ with $e \equiv j(a) \pmod{p^k}$;
5. for each $g \in \mathrm{Aut}_{\mathcal{O}}(\Omega_l)$ there is $s \in \mathrm{Gal}(\Omega_0/\mathbb{Q})$ with $s(A) = A$ and $g \circ j = j \circ s$;
6. for each $n$ and each $s \in \mathrm{Gal}(\Omega_0/\mathbb{Q})$ with $s(A) = A$ there is $g \in \mathrm{Aut}_{\mathcal{O}}(\Omega_l)$ with $g(q_n) = q_n$ and $g \circ j = j \circ s$.

So $j$ is a completion of $\Omega_0$ at $A$, and the decomposition group of $A$ is the image of the local Galois group.

**Definition 6.15.2 (Expansion map).** Let $j$ be a cusp embedding for $A$, $L \geq 0$, and $\psi$ a reparametrization at level $L$. An *expansion map* at level $L$ is a ring map $e : K_X(p^L) \to \Omega_l$ such that:

1. if $y \in K_X(p^L)$, $S \subseteq \Omega_0$ is finite, and every coefficient $y_r$ lies in $A$ and in $\mathbb{Q}(S)$, then there is $x' \in \Omega_l$ such that $\bigl(r \mapsto j(y_{r/p^L}),\, e(y),\, x'\bigr)$ is an evaluation for $\psi$;
2. if $g \in \mathrm{Aut}_{\mathcal{O}}(\Omega_l)$ fixes $q_L$, $s \in \mathrm{Gal}(\Omega_0/\mathbb{Q})$ satisfies $g \circ j = j \circ s$, and $y' = s(y)$ for the Galois action on $K_X$, then $g(e(y)) = e(y')$.

So $e$ sends a modular function to its $q$-expansion, read in the parameter $q_L$ and pushed into $\Omega_l$ by $j$.

### The theorem

**Theorem 6.15.3 (Logarithmic coordinates of a Siegel unit).** Assume that $\mathrm{an}(j_K)$ is the germ of a function holomorphic on $\mathcal{H}$. Let $p$ be an odd prime and $A$ a valuation ring of $\Omega_0$ with $p$ in its maximal ideal. Let $j$ be a cusp embedding for $A$, let $L \geq 1$, let $\psi$ be a reparametrization at level $L$, let $e$ be an expansion map at level $L$, and let $\iota$ be an embedding of $\mathcal{O}_L$. Let $N \geq 1$ be prime to $p$, put $M = Np^L$, and let $c > 1$ be prime to $6Np$. Let $A_1, a_2, g \in \mathbb{Z}$ with $a_2 \equiv Ng \pmod{p^L}$, $N \mid a_2$ and $M \nmid A_1$. Let $y \in K_X(p^L)$ be the Siegel unit $u_c(A_1, a_2)$ for $M$. Then there are a unit $w$ of $\mathcal{O}_L$, logarithmic coordinates $(\alpha, \beta)$ of $w$, and $z, z' \in \Omega_l$ with:

1. $\iota(w) = e(y)$;
2. $\bigl(r \mapsto j(F_c(A_1, a_2)_r)$ for $r \geq 0$ and $0$ for $r < 0,\ z,\ z'\bigr)$ is an evaluation for $\psi$;
3. $\iota(\alpha) \equiv -A_1 z \pmod{p^L}$;
4. $p\,\iota(\beta) \equiv -p\,g\,z \pmod{p^L}$.

Lean: `GlobalTheory.SiegLog.siegel_logCoords` (also `GlobalTheory.T.siegel_logCoords_alt`, a second name).

So $z$ is the value of the Eisenstein series $F_c(A_1, a_2)$ at $q_L$, and the theorem says $d\log y \equiv -F_c(A_1, a_2)\bigl(A_1\, d\log q_L + g\, d\log\zeta_L\bigr)$. The second congruence holds only after multiplication by $p$.

*Proof.* The proof has three steps.

*Step 1: a two variable expansion.* We use the following expansion of the Siegel unit. There is $\theta : \mathbb{Z} \times \mathbb{Z} \to \mathbb{Z}$ with these properties: for each $r$, $\theta(k, r) = 0$ for all large $|k|$; there is $r_0$ with $\theta(k, r) = 0$ for $r < r_0$; $\theta(k, r) \neq 0$ implies $p^L \mid r - A_1k$; for every $r$,
$$
y_{r/p^L} = \sum_k \theta(k, r)\,\zeta_{p^L}^{gk};
$$
and for every $r$,
$$
\sum_k k\,\theta(k, r)\,\zeta_{p^L}^{gk} = -\sum_{i \geq 0} F_c(A_1, a_2)_i\; y_{(r - i)/p^L}.
$$
Each $F_c(A_1, a_2)_i$ lies in $\mathbb{Z}[\zeta_{p^L}]$, and some coefficient $y_{r/p^L}$ equals $\pm\zeta_{p^L}^m$ for some $m$. Think of $y$ as the series $\sum_{k, r}\theta(k, r)X^{gk}Y^r$ in two variables. Then the last identity says that $X\frac{\partial}{\partial X}$ applied to $y$ is $-F_c \cdot y$, up to the factor $g$. The divisibility $p^L \mid r - A_1 k$ says that $Y\frac{\partial}{\partial Y}$ acts as $A_1$ times $X\frac{\partial}{\partial X}$ divided by $g$, modulo $p^L$. These two facts are the source of the two congruences.

*Step 2: the value $e(y)$.* All coefficients of $y$ lie in $A$ and in $\mathbb{Q}(\zeta_{p^L})$, since $\zeta_{p^L}$ and its inverse lie in $A$ by properties 1 and 3 of $j$. Property 1 of $e$ gives $x'$ such that $\bigl(r \mapsto j(y_{r/p^L}), e(y), x'\bigr)$ is an evaluation. One coefficient is $\pm\zeta_L^m$ after $j$, a unit. A lemma on evaluations with integral coefficients and a unit coefficient shows that $e(y) \neq 0$ and that $e(y)^{-1}$ is integral.

*Step 3: the unit of $\mathcal{O}_L$.* Apply $j$ to the identities of Step 1. They become identities for the coefficients of the evaluation of $e(y)$, with $\zeta_L$ in place of $\zeta_{p^L}$. A lemma on units with an integral two variable expansion then gives a unit $w$ of $\mathcal{O}_L$ with $\iota(w) = e(y)$, logarithmic coordinates $(\alpha, \beta)$ of $w$, and the evaluation $(j \circ F_c, z, z')$ with the two congruences. The first congruence comes from $r \equiv A_1 k \pmod{p^L}$; the second comes from the derivative identity, and it holds after multiplication by $p$. $\square$

**Remark 6.15.4 (Formalization).** The second name is a wrapper whose last alternative ends in `all_goals assumption` ([SiegelLogCoordsStatement.lean](lean:Development/AbelianVarietyTheory/Proofs/FoundationProofs/SiegelLogCoordsStatement.lean)). The holomorphy hypothesis on $j_K$ duplicates a field of the tower, as in earlier sections. Properties 2, 4, 5 and 6 of the cusp embedding and property 2 of the expansion map are not used in this proof; they are part of the data because the edge theorem of Section 12 needs them. The two variable expansion of Step 1, the lemma on evaluations with a unit coefficient and the lemma on units of $\mathcal{O}_L$ in Step 3 are `GlobalTheory.T.siegelUnitAtScaledArgument_twoVariableExpansion`, `GlobalTheory.T.evalSeries_cong_iff_coeff_and_isUnit` and `GlobalTheory.T.logCoords_unit_value_twoVariableIntegralExpansion`; we read them as statements.
