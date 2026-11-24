---
title: The projection derivative estimate
decls:
  - Formalism.MainNotions.PlaneGram.stmt
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The projection derivative estimate

This section states the lift bound of [the previous section](/entry/plane-gram-theorem-of-five-lemmas/) over a discrete valuation ring, with fixed constants $26$, $2$, $24$ and $60$. This form is the plane Gram input of [the closed second theorem](/entry/theorem-ii-closed-of-test-bound/) of Section 3, and it is used directly by [the concrete local bound](/entry/link-g-concrete5/) of Volume 15. We keep the notation of Section 1.

Let $\mathcal{O}$ be a [discrete valuation ring](/learn/commutative-algebra/#discrete-valuation-rings-and-lattices) of characteristic $0$, let $K$ be its fraction field, and let $p$ be a prime. We use the valuation $v$ on $K$ normalized by $v(p) = 1$.

**Definition 5.2.1 (Hida setting).** We say that $\mathcal{O}$ is in the *Hida setting at $p$* if it carries a uniformizer datum for $p$ and is an admissible discrete valuation ring for some integer $n' \geq 0$.

**Definition 5.2.2 (Signed chain data).** Let $r, J \geq 1$. *Signed chain data* over $\mathcal{O}$ consist of the following objects.

1. Segments indexed by $j \in \mathbb{Z}/J\mathbb{Z}$. Segment $j$ has $n_L(j)$ base letters, each with a sign (vector or covector), and $r$ twisted letters $(j, m)$, $m < r$.
2. A degree for each letter, and an exponent $g_{j,m}$ for each twisted letter.
3. For each $j$, a strictly increasing sequence of $n_j$ chains, which are sets of letters of segment $j$; each chain contains all $r$ twisted letters of the segment.
4. Thresholds $\theta_{j,i}$ and slopes $s_{j,i}$ for the chains, and link thresholds $\vartheta_{j,m}$ with $\vartheta_{j,m} > 0$ for $m + 2 \leq r$.
5. A function $\gamma$ from exponents to units of $\mathcal{O}$ such that, for each integer $k \geq 1$ and each sign $\varepsilon = \pm 1$, $\gamma^\varepsilon$ agrees modulo valuation $k$ with a combination $\alpha \mapsto \sum_m\lambda_m\prod_x\binom{\alpha_x}{m_x}$ with $\lambda_m \in \mathcal{O}$ and $\sum_x m_x \leq 6k$.
6. A real number $c \geq 1$.

These are the twist data of Section 1, with integral units and with the segments arranged in a cycle: the next segment after $j$ is $j + 1$ modulo $J$. The slope hypothesis with constant $C_H$ reads $r\,d_j/p^{g_{j,m}} + C_H\,r\,c \leq s_{j+1,i}$.

**Definition 5.2.3 (Projection derivative estimate).** Let $C_H$, $C_E$, $C_6$ and $C_{18}$ be numbers. The *projection derivative estimate* with these constants is the following statement. Let $r, J \geq 1$ and let signed chain data over $\mathcal{O}$ satisfy the slope hypothesis with $C_H$ and the size hypothesis $4(D_m + D_l + 3\kappa) < c$. Let $F$ be admissible input with $v_{\mathrm{BB}}(F) = 0$. Then there are model polynomials $G$ and $R$ such that:

1. $G$ is integral and satisfies the output conditions with $C_6$ and $C_{18}$;
2. $v(R_\alpha) \geq c - (D_m + D_l + C_E\kappa)$ for all $\alpha$;
3. the substitution $\phi$ maps all monomials of $G$ and $R$ into $\mathrm{Pol}_K(r, d_O)$;
4. $v_{\mathrm{BB}}\big(\phi(G + R)\big) \geq n_0 - \kappa$;
5. the pairing with the unit $\gamma$ satisfies
$$v\big(\langle F, \gamma\cdot\phi(G + R)\rangle\big) \leq D_m + D_l + C_E\kappa + \kappa + n_0.$$

**Definition 5.2.4 (Admissibility at a ring).** The ring $\mathcal{O}$ is *admissible* if it satisfies six conditions: an isotypic valuation condition, valuation stability, polynomial span, the Fock projector condition, the factorial digit split and the derivative congruence. The last five give Properties V2, SPAN, PROJ, DIG and DER of Section 1 for the field $K$.

**Theorem 5.2.5 (Plane Gram theorem).** Let $C_H \geq 26$. Let $\mathcal{O}$ be a discrete valuation ring of characteristic $0$ in the Hida setting at $p$, and assume that $\mathcal{O}$ is admissible. Then the projection derivative estimate holds with the constants
$$(C_H, C_E, C_6, C_{18}) = (C_H, 2, 24, 60).$$

Lean: `Formalism.MainNotions.PlaneGram.stmt`.

*Proof.* The Hida setting gives a uniformizer, and with it the normalized valuation $v$ on $K$. The second to sixth admissibility conditions give Properties V2, SPAN, PROJ, DIG and DER for $(K, v, p)$. By [the plane Gram theorem from five properties](/entry/plane-gram-theorem-of-five-lemmas/) with $C_0 = 1$, the uniform lift bound holds for $(K, v, p)$. A transfer lemma turns the uniform lift bound into the projection derivative estimate for signed chain data over $\mathcal{O}$, for every $C_H \geq 26$, with $C_E = 2$, $C_6 = 24$ and $C_{18} = 60$. $\square$

The first admissibility condition is not used. The constant $C_E = 2$ is the constant $2$ in $E = D_m + D_l + 2\kappa$ of the lift bound, and clause 5 is clause 5 of the lift bound.

**Remark 5.2.6 (Formalization).** The statement is `PlaneGramData.Stmt D CH 2 24 60` for all `D` and all `CH ≥ 26` (MonomialOrderSegments.lean:14). The parameter `D` is not used by `Stmt` or by `PlaneGramData.aux₃` (Lemma5aAt.lean:311, 316). The first part of `AdmAt` (Lemma5aAt.lean:137) is `IsotypicValuationAtRing`. The transfer `Br.plane_gram_of_theorem_at` (BrData.lean:723) was not unfolded. It passes from the lift constants $13$, $12$, $30$ to $26$, $24$, $60$; the reason for the factor $2$ was not checked. The bridges `second_valuation_of_admitted`, `brSPAN`, `brPROJ`, `brDIG` and `brDER` from the admissibility conditions to the five properties were not unfolded. Clause 5 is written as `EE CE + 2 * kp + n0 - kp` (Lemma5aAt.lean:309), which equals the bound above. The predicates `UniformizedDVR` and `AdmissibleDVR` of the Hida setting were not unfolded.
