---
title: The Lefschetz formula on charts
decls:
  - field0
  - UpperTheory.Cb.exists_chart_lift_of_finite_cover
  - UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_integral
status: drafted
drafted_by: writer@claude-opus-5-5
---
## The Lefschetz formula on charts

The holomorphic Lefschetz formula of Atiyah and Bott computes the alternating trace of a holomorphic map on [[Dolbeault cohomology|6GWRCGBGWC]] as a sum over its fixed points. This section and the next prove an algebraic form of it for a correspondence given by two finite étale maps $c_1, c_2 : Y \to Z$. Here we treat the case where $Z$ and $Y$ are integral. The proof moves the problem to the function fields of $Z$ and $Y$, and to Čech cohomology on the charts of a finite map $Z \to \mathbb{P}^d$. There the formula is a statement about traces of linear maps between modules of differential forms.

We first fix the objects of the formula. Let $Z$ be a scheme over $\mathbb{C}$ that is smooth of relative dimension $d$ and projective. For $a \geq 0$ let $H^b(Z, \Omega^a)$ be the [[sheaf cohomology|PQ6Q143ARJ]] of the sheaf of $a$-forms on $Z$. Let $c_1, c_2 : Y \to Z$ be [[finite|N9C4X7XKE4]] étale over $\mathbb{C}$. Then $c_2^* : H^b(Z, \Omega^a) \to H^b(Y, \Omega^a)$ is the pullback, and $c_{1*} : H^b(Y, \Omega^a) \to H^b(Z, \Omega^a)$ is the trace along the finite étale map $c_1$. The *correspondence* acts on $H^b(Z, \Omega^a)$ by $c_{1*} c_2^*$. A *fixed point* is a complex point $y$ of $Y$ with $c_1(y) = c_2(y)$.

**Definition (Cotangent matrix).** Let $y$ be a fixed point, and let $A$ be a complex $d \times d$ matrix. We say that $A$ is a *cotangent matrix* at $y$ if there are affine open sets $U \ni c_1(y)$ of $Z$ and $V \ni y$ of $Y$ and functions $t_1, \dots, t_d$ on $U$ such that the classes of $c_1^* t_1, \dots, c_1^* t_d$ in $\Omega_{Y, y} \otimes \mathbb{C}$ form a basis, and in this basis the class of $c_2^* t_j$ has coordinates the row $(A_{j1}, \dots, A_{jd})$.

So $A$ is the matrix of $c_2^*$ on cotangent vectors in the coordinates given by $c_1$. It is the transpose of the matrix of the tangent map. For a polynomial in $t$ we write $[t^a]$ for its coefficient of $t^a$. The number $[t^a] \det(1 + t A)$ is the trace of $\Lambda^a A$.

**Definition (Charts of a finite cover).** Let $F$ be a field over $\mathbb{C}$ with elements $x_0, \dots, x_d$, the function field of $\mathbb{P}^d$ in its homogeneous coordinates. A field $K$ over $F$ is a *finite cover on charts* if $K$ is finite and separable over $F$, and for each nonempty set $I$ of indices the ring $R_I(K)$ of the chart is smooth over $\mathbb{C}$. Here $R_I(K)$ is the ring of the part of the cover that lies over the intersection of the standard charts $x_i \neq 0$ for $i \in I$. The *Čech complex of $a$-forms* has in degree $p$ the product of the modules of $a$-forms $\Omega^a(R_I(K))$ over the sets $I$ with $p + 1$ elements, and $H^p_{\check{C}}(K, \Omega^a)$ is its cohomology.

**Theorem (Čech form of the Lefschetz formula).** Let $d, a \geq 0$, let $F \subseteq K \subseteq K'$ be fields over $\mathbb{C}$, and let $j_2 : K \to K'$ be a second map of $\mathbb{C}$-algebras. Suppose that $K$ and $K'$ are finite covers on charts for the same $x_0, \dots, x_d$. Suppose these conditions.
1. Over each chart, the cover $K'$ satisfies a covering condition with respect to $j_2$.
2. The fibre of $R_{\{0\}}(K')$ over the origin of chart $0$, the quotient by $x_1/x_0, \dots, x_d/x_0$, is reduced.
3. A fixed point is a $\mathbb{C}$-algebra map $e : R_I(K') \to \mathbb{C}$ such that $e \circ j_2$ and $e$ agree on $R_I(K)$. There are no fixed points on charts $i \neq 0$, and on chart $0$ each fixed point lies over the origin.
4. $\Phi$ is the finite set of fixed points in the fibre over the origin of chart $0$.
5. For each $e \in \Phi$ the matrix $A_e$ is the cotangent matrix at $e$: there are $c$ and $g_1, \dots, g_d$ in $R_{\{0\}}(K')$ with $e(c) \neq 0$, $c \cdot j_2(x_m/x_0) = \sum_l g_l \cdot x_l/x_0$, and $e(g_l) = e(c) (A_e)_{ml}$. Also $\det(1 - A_e) \neq 0$.
6. The maps $u_p$ on $H^p_{\check{C}}(K, \Omega^a)$ act as $c_{1*} c_2^*$: a cocycle $b$ lifts through $j_2$ to a cocycle on the charts of $K'$, and $u_p$ of the class of $b$ is the class of its trace from $K'$ to $K$.

Then
$$
\sum_{p=0}^{d} (-1)^p \operatorname{tr} u_p = \sum_{e \in \Phi} \frac{[t^a] \det(1 + t A_e)}{\det(1 - A_e)}.
$$

Lean: `UpperTheory.Cb.exists_chart_lift_of_finite_cover` (also `field0`, the private proof).

The Lean statement has two more hypotheses: regular parameters for $K$ at the fixed points, and finite dimension of the Čech groups. The proof does not use them, so we have left them out.

*Proof.* We give the proof in two cases.

First, let $a \leq d$. A theorem of the code proves the formula in this case from a list of about 95 named facts on Koszul complexes, filtrations, Čech and Koszul systems, edge maps and traces. Its proof starts from a top degree coefficient form and a Laurent constant term form on the function field, and it uses a fact that the residue of a trace is a sum over the fibre. We have not read the rest of it. To apply it, the proof packs the hypotheses into one structure, and in the cotangent condition it divides by $c$, which is allowed because $e(c) \neq 0$.

Second, let $a > d$. Then both sides are $0$. A lemma of the code gives a basis of $d$ logarithmic differentials for the $1$-forms on each chart and shows that the $a$-forms vanish, so each $u_p$ has trace $0$. On the right side, $\det(1 + t A_e)$ is a polynomial of degree at most $d$ in $t$, so its coefficient of $t^a$ is $0$. $\square$

**Theorem (Lefschetz formula, integral case).** Let $Z$ be an integral scheme over $\mathbb{C}$, smooth of relative dimension $d$ and projective. Let $Y$ be integral, and let $c_1, c_2 : Y \to Z$ be finite étale over $\mathbb{C}$. Let $\Phi$ be the finite set of fixed points, and for $y \in \Phi$ let $A_y$ be a cotangent matrix at $y$ with $\det(1 - A_y) \neq 0$. Then for each $a$ and $b$ the space $H^b(Z, \Omega^a)$ has finite dimension, and
$$
\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in \Phi} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.
$$

Lean: `UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_integral`.

*Proof.* We give the proof in six steps. The geometric inputs are lemmas of the code that we read only as statements.

First, $Y$ is smooth of relative dimension $d$, since $c_1$ is étale, and $H^b(Z, \Omega^a)$ has finite dimension because $Z$ is smooth and projective.

Second, let $K$ and $K'$ be the function fields of $Z$ and $Y$. The maps $c_1$ and $c_2$ give maps $K \to K'$ of $\mathbb{C}$-algebras. The first makes $K'$ an extension of $K$, and the second is $j_2$.

Third, choose a finite map $Z \to \mathbb{P}^d$ with these properties: the images in $Z$ of the fixed points lie in chart $0$ over the origin, and the fibre over the origin is reduced. This gives $F$, the elements $x_0, \dots, x_d$, and the affine charts of $Z$, so $K$ is a finite cover on charts. The same data, pulled back along $c_1$, make $K'$ a finite cover on charts.

Fourth, the complex points of the chart $c_1^{-1}(U_0)$ are the $\mathbb{C}$-algebra maps from its ring to $\mathbb{C}$. A point is a fixed point of $(c_1, c_2)$ if and only if the algebra map is a fixed point in the sense of the Čech form. This gives a bijection from $\Phi$ to the fixed points of the Čech form.

Fifth, at each fixed point, regular parameters give a matrix $A'_y$ that satisfies condition 5 of the Čech form. Two cotangent matrices at $y$ for different coordinates are conjugate, $A'_y = P A_y P^{-1}$. Conjugation does not change $\det(1 - A)$ or the coefficients of $\det(1 + t A)$.

Sixth, an isomorphism $E$ from $H^p(Z, \Omega^a)$ to the Čech group $H^p_{\check{C}}(K, \Omega^a)$, compatible with pullback and trace, comes from the Čech computation of coherent cohomology on the affine charts. Let $u_p = E \circ c_{1*} c_2^* \circ E^{-1}$. It has the lifting property of condition 6, and it has the same trace as $c_{1*} c_2^*$. The other conditions of the Čech form come from the lemmas of the third and fourth steps. The Čech form gives the formula with $A'_y$, and the fifth step replaces $A'_y$ by $A_y$. $\square$

**Remark.** The public name of the Čech form says "exists chart lift of finite cover", but the statement is a trace identity, not an existence statement. Its proof is the private theorem `field0`, and the step from the case $a \leq d$ to the full statement is a lemma `field0_of` ([TraceEqZeroOfBot.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/TraceEqZeroOfBot.lean#L49)). That lemma takes a hypothesis `ValBasic` that it does not use, and it binds the regular parameter hypothesis and the finite dimension hypothesis as `hgen` and `hfd` without using them. Its other bound names do not match their hypotheses: `hred` is the covering condition, `hnf` the reduced fibre, and `hz` the condition that charts $i \neq 0$ have no fixed points. The integral case proves the two unused hypotheses anyway, so no gap comes from them.

**Remark.** The definition of the chart rings $R_I(K)$, the Čech complex and the covering condition are not unfolded here. The [parent statement](/entry/t-exists-chart-lift-of-finite-cover/) of the Čech form is a renaming used in the chapter on Satake parameters, and the integral case is used in the next section.
