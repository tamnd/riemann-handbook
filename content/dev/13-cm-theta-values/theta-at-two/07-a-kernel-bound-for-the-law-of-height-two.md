---
title: A kernel bound for the law of height two
decls:
  - Formalism.L2.Th1.D.kernelOfF
  - Formalism.L2.Th1.D.kernel_of_f
status: drafted
drafted_by: writer@claude-opus-5-5
---
## A kernel bound for the law of height two

The last three sections of the chapter hold results at an odd prime $p$ that the proof uses next to the results at $2$. This section gives a bound for the frame jets of a theta kernel over an unramified field, in the coordinates of the formal group whose logarithm has terms only in the degrees $p^{2j}$. The [kernel bound](/entry/kernel-bound/) of the chapter on CM period valuations applies it, with the completion of the maximal unramified extension of $\mathbb{Q}_p$ as the field of coefficients. All objects here are formal power series over abstract fields; no curve appears.

**Definition 8.7.1 (Law of height two).** Let $p$ be a prime and $K$ a field of characteristic $0$ with an absolute value. A power series is *integral* if all its coefficients have absolute value at most $1$. Put $$\ell_p(X) = \sum_{j \geq 0} p^{-j} X^{p^{2j}} \in K[[X]].$$ Its linear coefficient is $1$, so it has a compositional inverse $e_p(X)$ with $e_p(0) = 0$. A series $F(X_0, X_1) \in K[[X_0, X_1]]$ is a *law with logarithm* $\ell_p$ if $F(0,0) = 0$, $F$ is integral, and $\ell_p(F(X_0, X_1)) = \ell_p(X_0) + \ell_p(X_1)$. For $c \in K$, a series $e(X)$ is a *multiplication by* $c$ if $e(0) = 0$ and $\ell_p(e(X)) = c\,\ell_p(X)$.

The degrees $1, p^2, p^4, \dots$ of $\ell_p$ are those of a logarithm of [height](/learn/formal-groups/#height) two. The multiplications by $c$ are the endomorphisms of $F$ over $K$ that act on the tangent space by $c$.

**Definition 8.7.2 (Equivalence modulo integral exponentials).** Let $f$ and $g$ be power series over $K$ in any set of variables. We write $f \simeq g$ if $f - g$ has constant term $0$ and $\exp(f - g)$ is integral.

The relation $\simeq$ says that $f$ and $g$ give the same integral structure after exponentiation: $\exp(f) = \exp(g)\,u$ with $u$ integral and $u(0) = 1$.

**Definition 8.7.3 (Frobenius lift).** Let $K_0$ be a field with an absolute value and $p$ a number. A ring map $\sigma : K_0 \to K_0$ is a *Frobenius lift at* $p$ if $p$ is a prime with $p > 2$, $|p| = p^{-1}$, every $a \neq 0$ has $|a| = p^k$ for some $k \in \mathbb{Z}$, and $|\sigma(a) - a^p| \leq p^{-1}$ for every $a$ with $|a| \leq 1$.

The last condition gives $|\sigma(a)| \leq 1$ when $|a| \leq 1$. So $\sigma$ preserves the closed unit ball and lifts the $p$-th power map of the residue field.

**Definition 8.7.4 (Kernel data).** Let $p$, $K_0$ and $\sigma$ be as above, and let $F$ be a law with logarithm $\ell_p$ over $K_0$. For $\beta \in K_0[[X_0, X_1]]$ put $$(\delta_F \beta)(X_0, X_1, X_2) = \beta(F(X_0, X_1), X_2) - \beta(X_0, X_2) - \beta(X_1, X_2),$$ and $\beta^\vee(X_0, X_1) = \beta(X_1, X_0)$. We say that $\beta$ is a *kernel series* for $(F, \sigma)$ if:

1. every coefficient of $\beta$ at a monomial $X_0^{n_0} X_1^{n_1}$ with $n_0 = 0$ or $n_1 = 0$ is $0$;
2. $\delta_F \beta \simeq 0$ and $\delta_F \beta^\vee \simeq 0$;
3. for every $\alpha \in K_0$ with $|\alpha| \leq 1$ and $\sigma^2(\alpha) = \alpha$, every multiplication $e$ by $\alpha$ and every multiplication $e'$ by $\sigma(\alpha)$, we have $\beta(e(X_0), X_1) \simeq \beta(X_0, e'(X_1))$.

Conditions 1 and 2 say that $\beta$ is additive in each variable for the law $F$, up to $\simeq$. Condition 3 says that $\beta$ is $\sigma$-sesquilinear for the endomorphisms of $F$, up to $\simeq$.

**Definition 8.7.5 (Theta substitution and frame jets).** Let $\nu \geq 1$, $r_0, r_1 \in \mathbb{N}$, and let $E$ be the set of triples $(r, a, b)$ with $0 \leq r < \nu$, $0 \leq a < r_0$ and $0 \leq b < r_1$. For $s \in \mathbb{Z}/2\nu$ let $\bar s \in \{0, \dots, 2\nu - 1\}$ be its representative; $s$ is *even* or *odd* as $\bar s$ is, and $\sigma^s$ means $\sigma^{\bar s}$. Let $\omega, \omega^* : \{0, \dots, \nu - 1\} \to K_0$, let $K$ be a second field and $j : K_0 \to K$ a ring map.

- For a series $\Xi$ over $K$ in the letters $X_{0,e}$ and $X_{1,e}$, $e \in E$, the *theta substitution* $\theta_Z(\Xi)$ is the series in the letters $Z_{s,a,b}$ ($s \in \mathbb{Z}/2\nu$, $0 \leq a < r_0$, $0 \leq b < r_1$) obtained by the substitution $$X_{0,(r,a,b)} \mapsto e_p\Big(\sum_{s \text{ even}} j(\sigma^s \omega^*_r)\, Z_{s,a,b}\Big), \qquad X_{1,(r,a,b)} \mapsto e_p\Big(\sum_{s \text{ odd}} j(\sigma^s \omega_r)\, Z_{s,a,b}\Big),$$ where $e_p$ is the inverse of $\ell_p$ over $K$.
- For $\beta$ over $K_0$, put $S_\beta = \sum_{e \in E} \beta^j(X_{0,e}, X_{1,e})$, where $\beta^j$ is $\beta$ with $j$ applied to its coefficients.
- A *frame* is a set $\mathcal{T} \subseteq \mathbb{Z}/2\nu$, numbers $C_s \in \mathbb{N}$ for $s \in \mathbb{Z}/2\nu$, heights $h_{s,c} \leq r_0$ for $0 \leq c < C_s$, and maps $I_{s,c} : \{0, \dots, h_{s,c} - 1\} \to \{0, \dots, r_1 - 1\}$. Take new variables $Y_{s,i,a}$ with $0 \leq i, a < r_0$, and put $R_{s,i,b} = \sum_a Y_{s,i,a} Z_{s,a,b}$. Let $P$ be the product over all $s$ and $c$ of the determinant of the $h_{s,c} \times h_{s,c}$ matrix $(R_{s,i,I_{s,c}(i')})_{i,i'}$. It is a polynomial in the $Z$ with coefficients in $K[Y]$.
- The *frame jet* of a series $\Theta$ in the $Z$ is $$J(\Theta) = \sum_\kappa P_\kappa\, \kappa!\, \Theta_\kappa \in K[Y],$$ where $\kappa$ runs over the monomials of $P$, $P_\kappa \in K[Y]$ and $\Theta_\kappa \in K$ are the coefficients at $Z^\kappa$, and $\kappa!$ is the product of the factorials of the exponents.

Since $\kappa!\,\Theta_\kappa$ is the derivative $\partial^\kappa \Theta(0)$, the frame jet applies to $\Theta$ the differential operator $P(\partial)$ in the $Z$, with coefficients that are minors of the generic matrices $(Y_{s,i,a})$.

**Definition 8.7.6 (Growth sums).** Let $p$, a frame and $r_0, r_1$ be as above. For $x \in \mathbb{N}$ let $\lg(x) = 0$ if $x = 0$ and $\lg(x) = \lfloor \log_p x \rfloor + 1$ otherwise. For $s \in \mathbb{Z}/2\nu$ put:

- $\alpha_s = \#\{c : h_{s,c} = 1\}$ if $s \in \mathcal{T}$, and $\alpha_s = 0$ if $s \notin \mathcal{T}$;
- $\gamma_s = C_s - \alpha_s$ and $\rho_s = \sum_c h_{s,c} - \alpha_s$ (differences in $\mathbb{N}$, cut at $0$);
- $D_s = \{\overline{s' - s} : s' \in \mathcal{T},\ s' \text{ and } s \text{ of different parity}\} \subseteq \mathbb{N}$.

Let $\mathcal{T}_{\mathrm{odd}}$ be the set of odd elements of $\mathcal{T}$, and put $$\delta = \sum_{s} \big(r_1 \lg(\alpha_s) + r_0 r_1 \lg(\rho_s)\big) + \sum_{s \in \mathcal{T}} \lg(\alpha_s)^2.$$ The *gain* and the *excess gain* are $$\begin{aligned} G &= \frac{p}{p^2 - 1} \sum_{s \in \mathcal{T}} \alpha_s - \sum_{s \in \mathcal{T}_{\mathrm{odd}}} \sum_{k \geq 0} \min\Big(\frac{\alpha_s}{p^{2k+1}},\ \gamma_{s + 2k + 1}\Big) - \delta, \\ G^{+} &= \sum_{s \in \mathcal{T}} \sum_{k \geq 0,\ 2k + 1 \notin D_s} \max\Big(\frac{\alpha_s}{p^{2k+1}} - \gamma_{s + 2k + 1},\ 0\Big) - \delta. \end{aligned}$$ The sums over $k$ converge, since their terms are at most $\alpha_s p^{-2k-1}$.

The number $\alpha_s$ counts the columns of height one at $s \in \mathcal{T}$, and $\gamma_s$ counts the other columns at $s$. In the gain, each column of height one counts $p/(p^2-1)$; for odd $s$ we subtract, at each odd shift $s + 2k + 1$, the smaller of $\alpha_s p^{-2k-1}$ and the number of other columns there. The term $\delta$ grows only like a logarithm of the sizes of the frame.

**Theorem 8.7.7 (Kernel bound for the law of height two).** Let $p$ be a prime. Let $K_0$ be a complete field of characteristic $0$ with an ultrametric absolute value, and $\sigma : K_0 \to K_0$ a Frobenius lift at $p$. Assume that $K_0$ contains a primitive $(p^2 - 1)$-th root of unity. Let $F$ be a law with logarithm $\ell_p$ over $K_0$ and $\beta$ a kernel series for $(F, \sigma)$. Let $K$ be a field of characteristic $0$ with an ultrametric absolute value and $j : K_0 \to K$ a ring map with $|j(a)| = |a|$ for all $a$, and assume that some $\varpi \in K$ has $\varpi^{p^2 - 1} = p$. Let $\nu \geq 1$, $r_0, r_1 \in \mathbb{N}$, and $\omega, \omega^* : \{0, \dots, \nu - 1\} \to K_0$ with:

1. $|\omega_r| \leq 1$, $|\omega^*_r| \leq 1$, $\sigma^{2\nu}(\omega_r) = \omega_r$ and $\sigma^{2\nu}(\omega^*_r) = \omega^*_r$ for all $r$;
2. $\sum_{s \text{ even}} \sigma^s(\omega_r \omega^*_{r'}) = 1$ if $r = r'$ and $0$ otherwise, the sum over the even $s \in \mathbb{Z}/2\nu$.

Let $U_0$ be an integral series and $\Phi$ a series with constant term $0$ in the letters $X_{0,e}, X_{1,e}$ over $K$, with $\Phi \simeq S_\beta$. Let a frame be given, with gain $G$, excess gain $G^{+}$ and numbers $\alpha_s$ as above, and let $c_n$ be the coefficient of a monomial $Y^n$ in $J(\theta_Z(\exp(-\Phi)\, U_0))$. Then:

1. $|c_n| \leq p^{-G^{+}}$;
2. $|c_n| \leq p^{-(G - A)}$, where $A$ is the sum of $\alpha_s$ over the even $s \in \mathcal{T}$;
3. for every integer $i \geq 1$, $|p^{m_i} c_n| \leq p^{-G}$, where $$m_i = \sum_{s \text{ even}} \sum_{c} \big(\min(h_{s,c}, i) - N_{s,c,i}\big) + \sum_{s \text{ odd}} \sum_c N_{s,c,i},$$ and $N_{s,c,i}$ is the number of $b < i$ in the image of $I_{s,c}$.

Lean: `Formalism.L2.Th1.D.kernelOfF` (also `Formalism.L2.Th1.D.kernel_of_f`, a second name).

The differences in $m_i$ are not negative: the image of $I_{s,c}$ has at most $h_{s,c}$ elements, and at most $i$ of them are below $i$. Bound 3 is the form in which the factor $|p|^{m_i} = p^{-m_i}$ can be moved to the right: it gives $|c_n| \leq p^{m_i - G}$.

*Proof.* We first put the theta substitution in rescaled coordinates. Since $j$ is isometric, $|p|_K = |p|_{K_0} = p^{-1}$, so $p \neq 0$ in $K$. As $p \geq 3$, $p^2 - 1 \geq 1$, so $\varpi^{p^2-1} = p \neq 0$ gives $\varpi \neq 0$. Put $$\lambda(X) = \varpi^{-1} \ell_p(\varpi X) = \sum_{j \geq 0} \varpi^{p^{2j} - 1} p^{-j} X^{p^{2j}}.$$ Its linear coefficient is $1$, so there is a series $\mu$ with $\mu(0) = 0$ and $\lambda(\mu(X)) = X$. Then $\ell_p(\varpi \mu(\varpi^{-1} u)) = \varpi \lambda(\mu(\varpi^{-1} u)) = u$, so $e_p(u) = \varpi \mu(\varpi^{-1} u)$. Hence $\theta_Z(\Xi)$ is the series obtained from $\Xi$ by the substitution $X_{0,(r,a,b)} \mapsto \varpi\, \mu\big(\sum_{s \text{ even}} j(\sigma^s \omega^*_r) Z_{s,a,b}\big)$ and $X_{1,(r,a,b)} \mapsto \varpi\, \mu\big(\sum_{s \text{ odd}} j(\sigma^s \omega_r) Z_{s,a,b}\big)$, followed by the change $Z \mapsto \varpi^{-1} Z$ of all letters. The coefficients of $\lambda$ have absolute value $p^{j - (p^{2j}-1)/(p^2-1)} \leq 1$, since $(p^{2j} - 1)/(p^2 - 1) = 1 + p^2 + \dots + p^{2j-2} \geq j$. This is why the rescaled form is the right one for integrality.

Next we turn the hypotheses into those of a bound for general systems of conjugates. Put $\omega_{r,s} = j(\sigma^s \omega_r)$ and $\omega^*_{r,s} = j(\sigma^s \omega^*_r)$ for $s \in \mathbb{Z}/2\nu$. These have absolute value at most $1$, since $\sigma$ preserves the unit ball. For $x = \sigma^{\bar s} \omega_r$ we have $|\sigma(x) - x^p| \leq p^{-1}$; at $\bar s = 2\nu - 1$ we use $\sigma^{2\nu} \omega_r = \omega_r$. So $|\omega_{r,s+1} - \omega_{r,s}^p| \leq p^{-1}$, and the same holds for $\omega^*$. Condition 2 says that the $\nu \times \nu$ matrices $M = (\sigma^s \omega_r)$ and $M^* = (\sigma^s \omega^*_{r'})$, with rows indexed by the $\nu$ even $s$, satisfy $M^{\mathsf T} M^* = 1$. Then $M^* M^{\mathsf T} = 1$, that is $\sum_r \sigma^a \omega^*_r\, \sigma^b \omega_r = 1$ if $a = b$ and $0$ otherwise, for even $a, b$. Applying $\sigma$ gives the same relation for odd $a, b$. Applying $j$ gives $\sum_r \omega^*_{r,a} \omega_{r,b} = 1$ if $a = b$ and $0$ otherwise, for $a$ and $b$ of the same parity.

For $\beta$, conditions 1 and 2 of a kernel series pass on unchanged. Let $\zeta \in K_0$ with $\zeta^{p^2-1} = 1$. Then $\sigma(\zeta)$ and $\zeta^p$ are both roots of $X^{p^2-1} - 1$, and $|\sigma(\zeta) - \zeta^p| \leq p^{-1}$. Two different roots $\eta, \eta'$ of this polynomial have $|\eta - \eta'| = 1$, since the product of $\eta - \eta'$ over $\eta' \neq \eta$ is $(p^2 - 1)\eta^{p^2-2}$, a unit. So $\sigma(\zeta) = \zeta^p$, and $\sigma^2(\zeta) = \zeta^{p^2} = \zeta$. The series $\zeta X$ is a multiplication by $\zeta$, because $\zeta^{p^{2j}} = \zeta$ gives $\ell_p(\zeta X) = \zeta \ell_p(X)$; in the same way $\zeta^p X$ is a multiplication by $\zeta^p$. Condition 3 now gives $\beta(\zeta X_0, X_1) \simeq \beta(X_0, \zeta^p X_1)$ for all such $\zeta$.

With these facts, the three bounds are a general kernel bound. It takes $p$, $K_0$, $\sigma$, the root of unity, $F$, $\beta$ with conditions 1 and 2 and the relation for the roots of unity, the isometry $j$, any families $\omega_{r,s}, \omega^*_{r,s}$ in $K$ with the three properties above, the element $\varpi$, a series $\mu$ with $\mu(0) = 0$ and $\lambda(\mu(X)) = X$, and $U_0$, $\Phi$ as in the theorem. It gives the three bounds for the frame jets of the rescaled substitution of $\exp(-\Phi) U_0$. By the first step this series is $\theta_Z(\exp(-\Phi) U_0)$. $\square$

**Remark 8.7.8 (Formalization).** The Frobenius lift of [IsLawOfLog.lean](lean:Formalism/ThetaLogCoordinates/UniformThetaSubstitution/IsLawOfLog.lean#L13) includes $p > 2$, so the theorem says nothing at $p = 2$ although it sits in the files on torsion integrality. The same definition of a Frobenius lift has a second copy in the files on hermitian frames, used in the next section. The proof in [ThetaIntegerIsSSubstitution.lean](lean:Formalism/LocalToGlobal/TorsionIntegrality/GaussSumParity/KummerThetaLogarithms/ThetaIntegerIsSSubstitution.lean#L250) gets $\mu$ from `logRescale`, which also proves facts on the size of $\lambda$ that are then discarded. The general kernel bound, `kernel_from_k_one_k` (equal to `kernel_bounds_generic`), was not unfolded; only its statement was read. The translation of the conditions on $\omega$ and $\beta$ is done by `omega_integral_criterion` and `betaHypOfF`, which were read as statements only; the arguments above are ours. The completeness of $K_0$ and the root of unity are passed to the general bound unchanged.
