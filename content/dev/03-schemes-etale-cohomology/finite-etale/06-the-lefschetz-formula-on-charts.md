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

The holomorphic Lefschetz formula of Atiyah and Bott computes the alternating trace of a holomorphic map on [[Dolbeault cohomology|6GWRCGBGWC]] as a sum over its fixed points. This section and the next prove an algebraic form of it for a correspondence given by two finite étale maps $c_1, c_2 : Y \to Z$. Here we treat the case where $Z$ and $Y$ are integral (Theorem 5.6.4). The proof moves the problem to the function fields of $Z$ and $Y$, and to Čech cohomology on the charts of a finite map $Z \to \mathbb{P}^d$. There the formula is a statement about traces of linear maps between modules of differential forms (Theorem 5.6.3). The next section removes the hypothesis that $Z$ and $Y$ are integral.

We first fix the objects of the formula. Let $Z$ be a scheme over $\mathbb{C}$ that is smooth of relative dimension $d$ and projective. For $a \geq 0$ let $H^b(Z, \Omega^a)$ be the [[sheaf cohomology|PQ6Q143ARJ]] of the sheaf of $a$-forms on $Z$. Let $c_1, c_2 : Y \to Z$ be [[finite|N9C4X7XKE4]] étale morphisms over $\mathbb{C}$. Then $c_2^* : H^b(Z, \Omega^a) \to H^b(Y, \Omega^a)$ is the pullback, and $c_{1*} : H^b(Y, \Omega^a) \to H^b(Z, \Omega^a)$ is the trace along the finite étale map $c_1$. The *correspondence* acts on $H^b(Z, \Omega^a)$ by $c_{1*} c_2^*$. A *fixed point* is a complex point $y$ of $Y$ with $c_1(y) = c_2(y)$.

**Definition 5.6.1 (Cotangent matrix).** Let $y$ be a fixed point, and let $A$ be a complex $d \times d$ matrix. We say that $A$ is a *cotangent matrix* at $y$ if there are affine open sets $U$ of $Z$ and $V$ of $Y$ with $y \in V \subseteq c_1^{-1}(U) \cap c_2^{-1}(U)$, and functions $t_1, \dots, t_d$ on $U$, with this property. Let $\mathfrak{m}_y$ be the ideal of $y$ in $\mathcal{O}(V)$. Then the classes of $d(c_1^* t_1), \dots, d(c_1^* t_d)$ form a basis of $\Omega^1(V) / \mathfrak{m}_y \Omega^1(V)$, and in this basis the class of $d(c_2^* t_j)$ has coordinates the row $(A_{j1}, \dots, A_{jd})$.

So $A$ is the matrix of $c_2^*$ on cotangent vectors in the coordinates given by $c_1$. It is the transpose of the matrix of the tangent map. For a polynomial in $t$ we write $[t^a]$ for its coefficient of $t^a$. The number $[t^a] \det(1 + t A)$ is the trace of $\Lambda^a A$.

**Definition 5.6.2 (Charts of a finite cover).** Let $F$ be a field over $\mathbb{C}$ with nonzero elements $x_0, \dots, x_d$ such that $x_1/x_0, \dots, x_d/x_0$ are algebraically independent over $\mathbb{C}$ and generate $F$ as a field over $\mathbb{C}$. So $F$ is the function field of $\mathbb{P}^d$ with homogeneous coordinates $x_0, \dots, x_d$. For a nonempty set $I$ of indices let $R_I(F) = \mathbb{C}[x_j/x_i : i \in I, \ 0 \leq j \leq d]$, the ring of the intersection of the standard charts $x_i \neq 0$ for $i \in I$. For a field $K$ over $F$ let $R_I(K)$ be the integral closure of $R_I(F)$ in $K$. We say that $K$ is a *finite cover on charts* if $K$ is finite and separable over $F$, and $R_{\{i\}}(K)$ is smooth over $\mathbb{C}$ for each $i$. The *Čech complex of $a$-forms* has in degree $p$ the product of the modules of $a$-forms $\Omega^a(R_I(K))$ over the sets $I$ with $p + 1$ elements, and $H^p_{\check{C}}(K, \Omega^a)$ is its cohomology.

If $Z \to \mathbb{P}^d$ is finite and $K$ is the function field of a normal $Z$, then $R_I(K)$ is the ring of the inverse image of the chart, which is why these rings are the right ones.

Let $j_2 : K \to K'$ be a map of $\mathbb{C}$-algebras. For a point $e : R_I(K') \to \mathbb{C}$ we say that an element $v \in K'$ is *regular at $e$ with value $c$* if there is $b \in R_I(K')$ with $e(b) \neq 0$, $b v \in R_I(K')$ and $e(b v) = e(b) c$. We say that $e$ is a *fixed point* if for each $b \in R_I(K)$ whose image in $K'$ lies in $R_I(K')$, the element $j_2(b)$ is regular at $e$ with value $e(b)$. For a set $J$ let $R^{(2)}_J$ be the integral closure in $K'$ of $j_2(R_J(K))$.

**Theorem 5.6.3 (Čech form of the Lefschetz formula).** Let $d, a \geq 0$, let $F \subseteq K \subseteq K'$ be fields over $\mathbb{C}$ with $x_0, \dots, x_d \in F$, and let $j_2 : K \to K'$ be a map of $\mathbb{C}$-algebras. Suppose that $K$ and $K'$ are finite covers on charts for $x_0, \dots, x_d$, and suppose these conditions.
1. For each $i$ and each point $e : R_{\{i\}}(K') \to \mathbb{C}$ there is $j$ such that each $v \in R^{(2)}_{\{j\}}$ satisfies: there is $b \in R_{\{i\}}(K')$ with $e(b) \neq 0$ and $b v \in R_{\{i\}}(K')$.
2. The ring $R_{\{0\}}(K') / (x_1/x_0, \dots, x_d/x_0)$, the fibre over the origin of chart $0$, is reduced.
3. There are no fixed points $e : R_{\{i\}}(K') \to \mathbb{C}$ for $i \neq 0$, and each fixed point on chart $0$ kills $x_1/x_0, \dots, x_d/x_0$.
4. $\Phi$ is a finite set of points of the fibre over the origin of chart $0$, and a point lies in $\Phi$ if and only if it is a fixed point.
5. For $e \in \Phi$ and $b \in R_{\{0\}}(K)$ with image in $R_{\{0\}}(K')$ and $e(b) = 0$, there are $c, g_1, \dots, g_d \in R_{\{0\}}(K)$, with the image of $c$ in $R_{\{0\}}(K')$ and $e(c) \neq 0$, such that $c b = \sum_l g_l \, x_l/x_0$.
6. For each $e \in \Phi$ and each $m$ there are $c, g_1, \dots, g_d \in R_{\{0\}}(K')$ with $e(c) \neq 0$, $c \, j_2(x_m/x_0) = \sum_l g_l \, x_l/x_0$, and $e(g_l) = e(c) (A_e)_{ml}$. Also $\det(1 - A_e) \neq 0$.
7. The maps $u_p$ on $H^p_{\check{C}}(K, \Omega^a)$ act as $c_{1*} c_2^*$: each cocycle $b$ lifts to a cocycle $\tilde b$ of the Čech complex of $a$-forms on the rings $R_I(K') R^{(2)}_J$, equal to $j_2(b_J)$ for $I = \emptyset$, and $u_p$ of the class of $b$ is the class of the trace from $K'$ to $K$ of the part of $\tilde b$ with $J = \emptyset$.
8. Each $H^p_{\check{C}}(K, \Omega^a)$ has finite dimension over $\mathbb{C}$.

Then
$$
\sum_{p=0}^{d} (-1)^p \operatorname{tr} u_p = \sum_{e \in \Phi} \frac{[t^a] \det(1 + t A_e)}{\det(1 - A_e)}.
$$

Lean: `UpperTheory.Cb.exists_chart_lift_of_finite_cover` (also `field0`, the private proof).

Condition 5 says that $x_1/x_0, \dots, x_d/x_0$ generate the maximal ideal of the image of $e$ in $R_{\{0\}}(K)$, after a localization. Condition 6 says that the matrix $A_e$ is the cotangent matrix of Definition 5.6.1 in the coordinates $x_l/x_0$. Condition 7 is the Čech form of the correspondence.

*Proof.* We give the proof in two cases.

First, let $a \leq d$. The formula comes from a residue computation on the function field $K$. On $K$ there are a top degree coefficient form, which takes a $d$-form to its coefficient in the basis $d(x_1/x_0) \wedge \dots \wedge d(x_d/x_0)$, and a constant term of Laurent expansions at the origin. The alternating trace of $u_p$ on Čech classes becomes a residue at the origin, through Koszul complexes on the charts and the edge maps of the Čech complexes. The residue of a trace from $K'$ to $K$ is the sum of the residues over the points of the fibre. By conditions 2, 3 and 4 this fibre sum is a sum over $\Phi$, and at $e \in \Phi$ the local term is $[t^a] \det(1 + t A_e) / \det(1 - A_e)$. In the cotangent condition one divides by $c$, which is allowed because $e(c) \neq 0$.

Second, let $a > d$. Then both sides are $0$. The $1$-forms on each chart have a basis of $d$ logarithmic differentials, so the $a$-forms vanish, and each $u_p$ has trace $0$. On the right side, $\det(1 + t A_e)$ is a polynomial of degree at most $d$ in $t$, so its coefficient of $t^a$ is $0$. $\square$

**Theorem 5.6.4 (Lefschetz formula, integral case).** Let $Z$ be an integral scheme over $\mathbb{C}$, smooth of relative dimension $d$ and projective. Let $Y$ be an integral scheme over $\mathbb{C}$, and let $c_1, c_2 : Y \to Z$ be finite étale morphisms over $\mathbb{C}$. Let $\Phi$ be a finite set of complex points of $Y$ such that $y \in \Phi$ if and only if $c_1(y) = c_2(y)$. For each $y \in \Phi$ let $A_y$ be a cotangent matrix at $y$ with $\det(1 - A_y) \neq 0$. Then for each $a$, each space $H^b(Z, \Omega^a)$ has finite dimension, and
$$
\sum_{b=0}^{d} (-1)^b \operatorname{tr}\bigl(c_{1*} c_2^* \mid H^b(Z, \Omega^a)\bigr) = \sum_{y \in \Phi} \frac{[t^a] \det(1 + t A_y)}{\det(1 - A_y)}.
$$

Lean: `UpperTheory.Cb.holomorphic_lefschetz_finiteEtale_integral`.

*Proof.* We give the proof in six steps.

First, $Y$ is smooth of relative dimension $d$, since $c_1$ is étale, and $H^b(Z, \Omega^a)$ has finite dimension because $Z$ is smooth and projective.

Second, let $K$ and $K'$ be the function fields of $Z$ and $Y$. The maps $c_1$ and $c_2$ give maps $K \to K'$ of $\mathbb{C}$-algebras. The first makes $K'$ an extension of $K$, and the second is $j_2$.

Third, choose a finite map $Z \to \mathbb{P}^d$ with these properties: the images in $Z$ of the fixed points lie in chart $0$ over the origin, and the fibre over the origin is reduced. This gives $F$, the elements $x_0, \dots, x_d$, and the affine charts of $Z$, so $K$ is a finite cover on charts. The same data, pulled back along $c_1$, make $K'$ a finite cover on charts. Conditions 1, 2, 3 and 5 of Theorem 5.6.3 follow from this choice.

Fourth, the complex points of the chart $c_1^{-1}(U_0)$ are the $\mathbb{C}$-algebra maps from its ring to $\mathbb{C}$. A point is a fixed point of $(c_1, c_2)$ if and only if the algebra map is a fixed point in the sense of Theorem 5.6.3. This gives a bijection from $\Phi$ to the fixed points in the fibre over the origin, which is condition 4.

Fifth, at each fixed point, the coordinates $x_l/x_0$ give a matrix $A'_y$ that satisfies condition 6. Two cotangent matrices at $y$ for different coordinates are conjugate, $A'_y = P A_y P^{-1}$. Conjugation does not change $\det(1 - A)$ or the coefficients of $\det(1 + t A)$.

Sixth, the Čech computation of coherent cohomology on the affine charts gives an isomorphism $E$ from $H^p(Z, \Omega^a)$ to the Čech group $H^p_{\check{C}}(K, \Omega^a)$, compatible with pullback and trace. So the Čech groups have finite dimension, which is condition 8. Let $u_p = E \circ c_{1*} c_2^* \circ E^{-1}$. It has the lifting property of condition 7, and it has the same trace as $c_{1*} c_2^*$. Theorem 5.6.3 gives the formula with $A'_y$, and the fifth step replaces $A'_y$ by $A_y$. $\square$

**Remark 5.6.5 (Formalization).** The name of Theorem 5.6.3 says "exists chart lift of finite cover", but the statement is a trace identity, not an existence statement. Its proof is the private theorem `field0`, and the step from the case $a \leq d$ to the full statement is `field0_of` ([TraceEqZeroOfBot.lean](lean:Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/LocalMaximality/TraceEqZeroOfBot.lean#L49)). That lemma takes a hypothesis `ValBasic` that it does not use, and it does not use conditions 5 and 8 either. Its bound names `hred`, `hnf` and `hz` stand for conditions 1, 2 and 3, so they do not match. The integral case proves conditions 5 and 8 anyway, so no gap comes from them. The case $a \leq d$ rests on a list of about 95 facts on Koszul complexes, filtrations, edge maps and traces; the sketch above is the outline of that argument, and we have not read all of it. The geometric inputs of the third to sixth steps of the proof of Theorem 5.6.4 were read as statements, not proofs.
