---
title: Word bounds on the big cell
decls:
  - GlobalTheory.T.wordBound_compactSupportCoefficients
  - GlobalTheory.HatNF.wordBound_cptCoef
  - GlobalTheory.T.wordBound_smooth_decaying_coefficients
  - GlobalTheory.HatNF.wordBound_decay
status: drafted
drafted_by: writer@claude-opus-5-5
---
## Word bounds on the big cell

This section moves the [radial word bound](/entry/word-bound/) from radial functions back to coefficients on $G$, at the big-cell points $\gamma(c)$. First we prove it for compactly supported coefficients, where the radial picture applies directly. Then we extend it to smooth coefficients that decay, with a multiplier that vanishes near the boundary and is a power of $G_f$ far from it. The second bound is the main input of the domination theorem of the next section.

### Cut words and the word bound

A letter of the place is a pair $(s, Y)$ with $s$ a sign and $Y \in \mathbb{R}$. Let $u, u'$ be the two parameters of the place and $l_0$ its level.

**Definition 5.3.1 (Cut word).** A real number $Y$ *lies on the cut* at $l_0$ if $u_{l_0} + 2 \le -Y \le u'_{l_0} - 2$ or $u'_{l_0} + 2 \le -Y \le u_{l_0} - 2$. A word $w$ is a *cut word* if each of its letters $(s, Y)$ has $Y$ on the cut, and two different letters $(s, Y)$, $(s', Y')$ of $w$ have $|Y - Y'| > 2$.

So the points of a cut word lie strictly between the two parameters and are well separated. A cut word is nonempty only if $|u_{l_0} - u'_{l_0}| \ge 4$.

For a coefficient $F$ and a local point $\gamma$, let $V_p(F)(\gamma)$ be the vector of $F$ at $\gamma$, a finite family of Hilbert-Schmidt operators, and write $\|V_p(F)(\gamma)\|$ for the norm of the family. For a word $w$ and an index $e$, let $\Theta_{w,e}$ be the operator of the place attached to $w$ and $e$. For a function $\varphi$ on $\mathbb{R}$ let $\varphi \cdot_G F$ be the coefficient $g \mapsto \varphi(G_f(g)) F(g)$. We have not unfolded $V_p$ or $\Theta_{w,e}$.

**Definition 5.3.2 (Word bound).** Let $a, J \in \mathbb{N}$, $C \in \mathbb{R}$, $w$ a word, $\Theta_1, \dots, \Theta_m$ differential operators, and $K$ a condition on pairs $(\varphi, f)$ of a function and a coefficient. The *word bound* holds if $C \ge 0$, each $\Theta_i$ is polynomial of type $(|w|\,n,\ |w| \cdot 8(r+1)n)$, and for every pair $(\varphi, f)$ that satisfies $K$, every index $e$ and every $c \in \mathbb{C}^{r+1}$ with all $c_l \ne 0$ and $G_p(\gamma(c)) > 0$,
$$\begin{aligned}\|V_p(\Theta_{w,e}(\varphi \cdot_G f))(\gamma(c))\| \le{}& C\, \Bigl|\prod_l c_l\Bigr|^{-|w|}\, G_p(\gamma(c))^{-a|w|} \\ &\times \sum_{j=0}^{J} |\vartheta^j\varphi(G_p(\gamma(c)))| \sum_{i=1}^{m} \|V_p(\Theta_i f)(\gamma(c))\| .\end{aligned}$$

### Compactly supported coefficients

A *compactly supported coefficient* of the place is a coefficient with compact support on which the radial picture is defined. We have not unfolded this class.

**Theorem 5.3.3 (Word bound for compact support).** Let $a : \mathbb{N} \to \mathbb{N}$ be such that the basic elements [lift with loss $a$](/entry/basic-lift-all-zero/). Let $p$ be a place datum and $w$ a cut word. Then there are $C$, $J$ and differential operators $\Theta_1, \dots, \Theta_m$ such that the word bound holds with exponent $a(r)$ for the condition: $\varphi$ is smooth and $f$ is a compactly supported coefficient.

Lean: `GlobalTheory.HatNF.wordBound_cptCoef` (also `GlobalTheory.T.wordBound_compactSupportCoefficients`, a second name).

*Proof.* The actual operators of the place have normal form data $d$. A cut word gives an admitted word for the radial picture. Apply the [radial word bound](/entry/word-bound/) with $T$ the set of polynomial lifts of type $(n, 8(r+1)n)$ and the exponent $a(r)$; its hypothesis is the lifting of basic elements. It gives $C$, $J$ and lists $H_1, \dots, H_m$ of $|w|$ polynomial lifts.

A product of $N$ polynomial lifts of type $(n, 8(r+1)n)$ is a polynomial lift of type $(Nn, N \cdot 8(r+1)n)$, since composing differential operators adds the orders and multiplying polynomials adds the degrees. So each product $\prod H_i$ is the radial part of a polynomial operator $\Theta_i$ of the type that the word bound asks for.

Now let $\varphi$ be smooth and $f$ compactly supported. The coefficient $\varphi \cdot_G f$ is again compactly supported, and its radial function is $W_0\Phi$, where $\Phi$ is a radial function of $f$ and $W$ is the multiplier family of $\varphi$. At a big-cell point $\gamma(c)$ the norm of the vector of a coefficient equals the norm of the value of its radial function at the matching radial point, up to a fixed factor. At that point $d_R = |\prod_l c_l|$ and $g_R = G_p(\gamma(c))$. So the radial bound, read at the matching point, is the word bound. $\square$

### Smooth coefficients that decay

A coefficient $f$ is *smooth* if it is $C^\infty$ on $G$. For $A \in \mathbb{R}$ and $m \in \mathbb{N}$ the *decay class* of order $A$ and depth $m$ is a class of coefficients whose derivatives of order at most $m$ decay at rate $A$; we have not unfolded it. A place satisfies the *decomposition condition* at level $C_b$ when its word operators decompose into differential operators of bounded order; we have not unfolded this either.

**Definition 5.3.4 (Cut power).** Let $e \in \mathbb{N}$. A function $\varphi : \mathbb{R} \to \mathbb{R}$ is a *cut power of degree $e$* if $\varphi$ is smooth, $\varphi(x) = 0$ for $x < \delta$ for some $\delta > 0$, and $\varphi(x) = a x^e$ for $x \ge R$, for some $a$ and $R$.

The example to keep in mind is $\varphi(y) = \chi(y/\varepsilon)\, y^{p_0}$, with $\chi$ a cutoff. It vanishes near the boundary and is the power $y^{p_0}$ away from it.

**Theorem 5.3.5 (Word bound for decaying coefficients).** Let $a : \mathbb{N} \to \mathbb{N}$ be such that the basic elements lift with loss $a$. For every $C_b$ there is $C_c$ with this property. Let $p$ be a place datum that satisfies the decomposition condition at level $C_b$, let $N \in \mathbb{N}$, and let $w$ be a cut word with $|w| \le N$. Then there are $C$, $J$ and $\Theta_1, \dots, \Theta_m$ such that the word bound holds with exponent $a(r)$ for the condition: there are $e \in \mathbb{N}$ and $A \in \mathbb{R}$ such that $\varphi$ is a cut power of degree $e$, $f$ is smooth, $f$ lies in the decay class of order $A$ and depth $m$ for every $m$, and
$$C_c\,(r+1)^4\,(N n^2 + n^3) \le A - (2r+2)e .$$

Lean: `GlobalTheory.HatNF.wordBound_decay` (also `GlobalTheory.T.wordBound_smooth_decaying_coefficients`, a second name).

The inequality is a margin: the decay of $f$ must beat the growth of $\varphi$ and of the derivatives along a word of length $N$.

*Proof.* Take $C$, $J$ and $\Theta_i$ from the [compact support case](/entry/word-bound-cpt-coef/). They do not depend on $\varphi$ or $f$. Take $C_c = 5\max(C_b, 8) + \max(C_b, 8)^2 + 1 + |\max(c_1, c_2)|$, where $c_1$ and $c_2$ are the constants of two limit lemmas below.

Fix $(\varphi, f)$ with the condition, an index $e$ and a point $\gamma = \gamma(c)$ with all $c_l \ne 0$ and $G_p(\gamma) > 0$. Let $\varphi$ vanish below $\delta_0$, and put $\delta = \min(\delta_0, G_p(\gamma)/2)$. Fix a cutoff $\chi$ and let $\beta_k$ be the smooth bump functions of radius about $k$ on $G$. The coefficients
$$f_k = \beta_k \cdot \mathrm{cut}(\chi, f, \delta), \qquad \mathrm{cut}(\chi, f, \delta)(g) = \chi(G_f(g)/\delta) f(g),$$
are compactly supported. The compact support case applies to $(\varphi, f_k)$. Since $\varphi(G_f) \ne 0$ only where $G_f \ge \delta_0 \ge \delta$, and $\chi = 1$ there, we have $\varphi \cdot_G f_k = \beta_k\, (\varphi \cdot_G f)$.

Let $k \to \infty$. The first limit lemma, with constant $c_2$, shows that the vectors at $\gamma$ of $\Theta_{w,e}(\beta_k (\varphi \cdot_G f))$ converge to that of $\Theta_{w,e}(\varphi \cdot_G f)$. The second, with constant $c_1$, shows that the vectors of $\Theta_i f_k$ converge to those of $\Theta_i f$, since $G_p(\gamma) \ge 2\delta$. Both lemmas need decay of $f$ beyond the growth of $\varphi$, and the margin with $C_c$ gives it. The bound passes to the limit. $\square$

**Remark 5.3.6 (Formalization).** The compact case is in [WordBoundCompactSupportCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundCompactSupportCoefficients.lean#L29); the closure of polynomial lifts under products is `polyLift_listProd` at line 17. The decaying case is in [WordBoundSmoothDecayingCoefficients.lean](lean:Development/AbelianVarietyTheory/Proofs/JetHarmonics/WordBoundSmoothDecayingCoefficients.lean#L18). The two limit lemmas are `vecV_cut_op` and `vecV_cut_polyOp`, which we did not open; the text above states only how they are used. The word bound is `WordBound` in [BasicLiftAll.lean](lean:Development/AbelianVarietyTheory/Definitions/Jets/BasicLiftAll.lean#L38). We have not unfolded `CptCoef`, `InCC` or `InDDplus2`.
