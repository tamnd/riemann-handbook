---
id: least-value-le
title: A bound for the least value of theta generators over a level prime
kind: theorem
decl: GlobalTheory.LevelPrimePoint.least_value_le
module: Development.AbelianVarietyTheory.Proofs.JetHarmonics.ThetaGeneratorsLeastValueOverLevelPrime
covers: 486
status: drafted
drafted_by: writer@claude
---
This theorem bounds, at an integral point over a complete discrete valuation ring, the least valuation of a theta generator of weight $a$. The bound is $\mathrm{DF}(a)\,v(g)/(g-1)$ plus two small terms, divided by the ramification index $e$. Its one hypothesis is `HTFSt`, which enters through [`T.depthBelowOne_of_hodgeTate_chart_form`](/entry/depth-below-one-of-hodge-tate-chart-form/). The theorem lies below the step [EveryCharacter from the literature](/step/every-character-of-literature/).

## Statement

Let $E$ be a CM field with host $H$, datum $D_w$ of signature $(p, q)$, level $l$, moduli $X_o$ and coefficients $c$. Write $\mathrm{DF}(a) = \sum_\tau \sum_{i < m_\tau} a(\tau, i)$, with $m_\tau$ = `Dw.mult τ`.

- A *theta generator* $f \in \mathrm{thGen}(a, n)$ is a rule for which there are $x \in \Lambda^n$ and a polynomial $P$ in the harmonic set `harmA a n` such that at every point the value of $f$ is the theta value of $(x, P)$. We have not unfolded the theta value `ThValAt`.
- For a complete discrete valuation ring $T$ of characteristic $0$, $v_T$ is its normalized valuation and $\mathrm{nval}_e(x) = v_T(x)/e$, with $\mathrm{nval}_e(0) = \infty$.
- $\mathrm{ev}(y, f)$ (`evI`) is the value of the rule $f$ at the integral point $y$.

**Theorem.** Assume `HTFSt p` for every prime $p$. Let $\nabla$ be a theta value map with `IsNab` and `ThValTot`. Let $y$ be an integral point over $T$ with finite residue field, with a chart $C$, a truncation `FrTrunc` and a uniformisation $P$ with `TorsionIso`. Let $\varpi$ be a uniformizer, $Q$ an integer function on the character lattice with `IsQ`, and $b_1, \dots, b_r$ a basis with $Q(b_j) \le \Phi$ and $|Q(b_j+z) - Q(b_j) - Q(z)| \le M_0 Q(z)$. Let $g \ne g'$ be primes with:

- $l.M = g'g$, $\pi\bar\pi = g$, $\pi'\bar\pi' = g'$ and $l.M_b = (\pi\pi')$;
- $g$ splits completely in $E$ and is not a unit in $T$.

Let $a$ be antitone in $i$ for each $\tau$, with $n \ge 2(p+q)$, $n \ge 1$, $e > 0$, $\mathrm{DF}(a) < g-1$, $4\,\mathrm{DF}(a) + 4 \le g'$ and $\mathrm{DF}(a)\,M_0 < g'$. Then

$$\begin{aligned}&{\inf_{f \in \mathrm{thGen}(a,n)} \mathrm{nval}_e(\mathrm{ev}(y, f)) + \mathrm{nval}_e\Bigl(\prod_\tau \iota\bigl(\tau(\bar\pi\bar\pi')\bigr)^{\sum_i a(\tau,i)}\Bigr)}\\ &{\quad \le \frac{1}{e}\Bigl(\frac{v_T(g)\,\mathrm{DF}(a)}{g-1} + \frac{(p+q)\,r\,\Phi}{4g'} + \frac{2\,\mathrm{DF}(a)^2\,\Phi}{g'}\Bigr).}\end{aligned}$$

## Proof

1. The coprimality of the level gives Bezout relations for $\pi\pi'$ and $\bar\pi\bar\pi'$, and for $\pi, \bar\pi$.
2. Extend $T$ to an algebraically closed valued field $F$ with valuation $v$ and ring $O$. Take a Tate isometry for the chart and power data on $(p+q) + n_2$ copies.
3. For each $\tau$, exactly one of $v(\tau\bar\pi) > 0$ and $v(\bar\tau\bar\pi) > 0$ holds. This gives a choice of type for each $\tau$.
4. `exists_minor_harm` gives a polynomial in `harmA` that is a product of leading minors of total degree $\mathrm{DF}(a)$.
5. `T.depthBelowOne_of_hodgeTate_chart_form`, with `HTFSt`, bounds the valuation $\rho$ of this minor product by the right side above.
6. `T.pointStatements_on_copies_hold` writes the value of valuation $\rho$ as $\sum_i a_i z_i$ with $v(a_i) \ge 0$. `exists_val_le` picks $i$ with $v(z_i) \le \rho$.
7. `T.value_translate_pullback_eq_generator'` gives $z_i = \varepsilon A\, \mathrm{ev}(y, f)$ with $f \in \mathrm{thGen}(a, n)$. `nval_add_le` turns this into the bound for the infimum.

## In the Lean code

The theorem is in [ThetaGeneratorsLeastValueOverLevelPrime.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/ThetaGeneratorsLeastValueOverLevelPrime.lean#L196). The helpers `exists_minor_harm`, `exists_val_le`, `nval_add_le` and `exists_sec_cast` are at lines 57, 156, 166 and 181. `thGen` and `harmA` are in [IsThRule.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/IsThRule.lean#L86), and `DF` is in [ThProps.lean](lean:Formalism/LocalToGlobal/ProjectiveLattices/ThProps.lean#L28).

`HTFSt` is used only at line 270. In the caller `refExp_level_le_one`, it is filled by `ChF.hodgeTate_inclusion_chart`. We have not unfolded `IsNab`, `IsQ`, `FrTrunc` or `TorsionIso`.
